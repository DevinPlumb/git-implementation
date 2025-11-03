import argparse
import configparser
from datetime import datetime
import grp, pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib

argparser = argparse.ArgumentParser(description="The stupidest content tracker")

argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

def cmd_add(args):
    print("add: not implemented")

def cmd_cat_file(args):
    print("cat-file: not implemented")

def cmd_check_ignore(args):
    print("check-ignore: not implemented")

def cmd_checkout(args):
    print("checkout: not implemented")

def cmd_commit(args):
    print("commit: not implemented")

def cmd_hash_object(args):
    print("hash-object: not implemented")

def cmd_init(args):
    print("init: not implemented")

def cmd_log(args):
    print("log: not implemented")

def cmd_ls_files(args):
    print("ls-files: not implemented")

def cmd_ls_tree(args):
    print("ls-tree: not implemented")

def cmd_rev_parse(args):
    print("rev-parse: not implemented")

def cmd_rm(args):
    print("rm: not implemented")

def cmd_show_ref(args):
    print("show-ref: not implemented")

def cmd_status(args):
    print("status: not implemented")

def cmd_tag(args):
    print("tag: not implemented")

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add"          : cmd_add(args)
        case "cat-file"     : cmd_cat_file(args)
        case "check-ignore" : cmd_check_ignore(args)
        case "checkout"     : cmd_checkout(args)
        case "commit"       : cmd_commit(args)
        case "hash-object"  : cmd_hash_object(args)
        case "init"         : cmd_init(args)
        case "log"          : cmd_log(args)
        case "ls-files"     : cmd_ls_files(args)
        case "ls-tree"      : cmd_ls_tree(args)
        case "rev-parse"    : cmd_rev_parse(args)
        case "rm"           : cmd_rm(args)
        case "show-ref"     : cmd_show_ref(args)
        case "status"       : cmd_status(args)
        case "tag"          : cmd_tag(args)
        case _              : print("Bad command.")