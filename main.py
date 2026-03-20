# compiler for flart, a simple domain-specific programming language for
# describing workflows or processes.
# Copyright (C) 2026  mfnz

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import graphviz as gv

program = """
lamp doesnt work:
  lamp plugged in? |
  plug in lamp &
  bulb burnt out? &
  @replace bulb |
  repair lamp;

replace bulb:
  remove bulb;
  dispose of bulb responsibly;
  install replacement bulb;
"""

print("program:", program, sep="\n")

def lexer(code):
    symbols = "&","|","@",":",";"
    lexeme = ""
    lexemes = list()

    for char in code:
        if char in symbols:
            if lexeme.strip() != "":
                lexemes.append(lexeme.strip())
            lexemes.append(char)
            lexeme = ""
        else:
            lexeme += char
    if lexeme.strip() != "":
        lexemes.append(lexeme.strip())

    lexemes.append("\0")

    return lexemes

program = lexer(program)

print("lexer: ", program, sep="\n")

def collect_until(tokens, i, stop_tokens):
    collected = []
    while i < len(tokens) and tokens[i] not in stop_tokens:
        collected.append(tokens[i])
        i += 1
    return collected, i

def parser(tokens):
    nodes = {}
    n_content, n_type = False, False
    i = 0
    while i < len(tokens):
        token = tokens[i]
        match token:
            case "&" | "|":
                branch = {}
                while tokens[i] in ("&","|"):
                    order = ("&","|") if token == "&" else ("|","&")
                    collected, i = collect_until(tokens, i+1, order[1])
                    branch[order[0]] = parser(collected)
                    collected, i = collect_until(tokens, i+1, ("&","|",":"))
                else:
                    i-=1
                    collected.pop()
                    branch[order[1]] = parser(collected)
                    n_type = "if", branch
            case ":":
                n_type = "label"
            case ";":
                n_type = "pass"
            case "@":
                n_type = "call"
            case "\0":
                n_type = "EOF"
                n_content = "\0"
            case _:
                n_content = token
        if n_type and n_content:
            nodes[n_content] = n_type
            n_content, n_type = False, False
        i += 1
    return nodes

program = parser(program)

print("parser:", program, sep="\n") 

def interpreter(ast):
    graph = gv.Digraph("graph")
    gv_nodename = {}
    for n_content, n_type in ast.items():
        inc_node = lambda t : 1 if t in gv_nodename.keys() else 0
        gv_node = lambda t, label : graph.node(f"{t}{gv_nodename[t]}", label)
        match str(type(n_type)):
            case "<class 'str'>":
                gv_nodename[n_type] = inc_node(n_type)
                gv_node(n_type, n_content)
                match n_type:
                    case "label":
                        pass
                    case "pass":
                        pass
                    case "call":
                        pass
                    case "EOF":
                        pass
                    case _:
                        print("unknown node type encountered:", n_type)
            case "<class 'tuple'>":
                gv_nodename[n_type[0]] = inc_node(n_type[0])
                gv_node(n_type[0], n_content)
                match n_type[0]:
                    case "if":
                        pass
                    case _:
                        print("unknown node type encountered:", n_type)
            case _:
                print(f"node {n_content} contains data of type {type(n_type)}")
    return graph

program = interpreter(program)

print("interpreter:", program.source, sep="\n")
