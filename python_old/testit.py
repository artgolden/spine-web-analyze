''''testit.py tests python scripts by submitting input strings and comparing output strings to pattern.
Test are provided inside script comments #test: 'input string' 'output string'
'''

import re, sys, subprocess

def run_test( file_name, input_string, output_string ):
	ENC = 'utf-8'
	p = subprocess.Popen( ['python3', file_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE )
	i_b = bytes( input_string + '\n', ENC )
	o_b, err_b = p.communicate( i_b )
	p.wait
	if o_b:
		out = str(o_b, ENC).strip()
	else:
		out = ''
	if err_b:
		out_err = str(err_b, ENC).strip()
	else:
		out_err = ''

	if out == output_string:
		print( 'OK: "' + input_string + '" -> "' + out + '" == "' + output_string + '"' )
	else:
		print( 'FAIL: "' + input_string + '" -> "' + out + '" != "' + output_string + '" ERR="' + out_err + '"' )

def run_tests( file_name ):
	p0 = re.compile( '''#test:''' ) 
	p = re.compile( '''#test:[\s#]*(?:[']([^']+)[']|["]([^"]+)["])[\s#]*(?:[']([^']+)[']|["]([^"]+)["])''', re.MULTILINE )
	f = open( file_name )
	ml = None
	ln = 0
	start_ln = 0
	for l in f:
		ln += 1
		r0 = p0.match( l )
		if r0:
			if ml:
				print('Error in test lines ' + str(start_ln) + ".." + str(ln-1) + ':"' + ml + '"')
			ml = l
			start_ln = ln
		elif ml:
			ml += l
		if ml:
			r = p.match( ml )
			if r is not None:
				if r.group(1):
					input_string = r.group(1)
				else: 
					input_string = r.group(2)
				input_string = input_string.replace('#', '')
				if r.group(3):
					output_string = r.group(3)
				else: 
					output_string = r.group(4)
				output_string = output_string.replace('#', '')
				run_test( file_name, input_string, output_string )
				ml = None
				start_line_number = 0
	if ml:
		print('Error in test lines ' + str(start_ln) + ".." + str(ln-1) + ':"' + ml + '"')

tests = run_tests( sys.argv[1] )

