#!/usr/bin/python
import tarfile
import os
import sys
import functools
import getopt

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

def run(path):
	cmd=os.path.join(path,"install")
	if not os.path.isfile(cmd):
		return
	os.system(cmd)
	os.remove(cmd)


def main():
	try:
		opts,args=getopt.getopt(sys.argv[1:],'hf:',["help","file="])
	except getopt.GetoptError:
		print "getopt error"
		usage()
		sys.exit(1)
	path=os.getcwd()
	for opt,arg in opts:
		if opt in ("-h","--help"):
			usage()
			sys.exit()
		elif opt in ( "-f","--file"):
			tarfile=arg
	if len(tarfile) ==0:
		print "cannot find tarfile"
		usage()
		sys.exit(3)
	if len(args) == 1:
		path=args[0]
	install(tarfile,path)
	run(path)


if __name__ == "__main__":
	main()
