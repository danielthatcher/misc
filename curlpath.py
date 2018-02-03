#! /usr/bin/env python3

from lxml import html,etree
import argparse
import requests


if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Parse a html page with xpath")
    parser.add_argument("xpath", help="The xpath to use")
    parser.add_argument("uri", help="The URI of the page to parse")
    parser.add_argument("-p", "--pretty-print", help="Pretty print elements", action="store_true", default=False)
    parser.add_argument("-e", "--encoding", default="UTF-8", help="The encoding to use. Default is UTF-8")
    args = parser.parse_args()

    # Get and parse page
    response = requests.get(args.uri)
    tree = html.fromstring(response.content)
    nodes = tree.xpath(args.xpath)
    for n in nodes:
        if type(n) == html.HtmlElement:
            n = etree.tostring(n, pretty_print=args.pretty_print).decode(args.encoding)

        print(n)
