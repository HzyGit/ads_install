#!/usr/bin/python
import tarfile
import os
import sys
import functools

def install(tarf,dest):
	tar=tarfile.open(tarf,"r:gz");
	extract=functools.partial(tar.extract,path=dest);
	map(extract,tar.getnames());

def usage():
	print "Usage: install [options] [path]"
	print "install tar file in path"
	print ""
	print "options:"
	print "\t -h,--help                display this information"
	print "\t -f,--file tarfile        use tarfile to update system"
	print "\t path                     the destintion path"

def test():
	install(sys.argv[1],sys.argv[2])

def main():
	test()

if __name__ == "__main__":
	main()
