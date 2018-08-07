#!/usr/bin/env python

import os
import sys
import pkg_resources

from grpc_tools import protoc


def compile(name):
    proto_include = pkg_resources.resource_filename('grpc_tools', '_proto')

    protoc.main([
        "protoc",
        "--python_out=.",
        "--grpc_python_out=.",
        "./_proto/{}.proto".format(name),
        "--proto_path=./_proto/",
        "--proto_path={}".format(proto_include)
    ])


def main():
    compile('chat')


if __name__ == '__main__':
    sys.exit(main())
