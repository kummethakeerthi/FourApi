from flask import Flask, request, jsonify
app = Flask(__name__)


def intFloatCasting(str1):
	if str1.isdigit():
		return int(str1)
	if '.' in str1:
		try :
			return float(str1)
		except Exception as e:
			return "error"
	else:
		return "error"





@app.route('/add', methods=['get'])
def create_cm():
		one = request.args.get('one', None)
		two = request.args.get('two', None)
		value1 =intFloatCasting(one)
		print value1
		value2 =intFloatCasting(two)
		print value2
		if isinstance(value1, str) or isinstance(value2, str):
			return "invalid values"
		else :
			value3=value1+value2
			value3=str(value3)
			return value3

@app.route('/div', methods=['get'])
def create_cm1():
		one = request.args.get('one', None)
		two = request.args.get('two', None)
		value1 =intFloatCasting(one)
		print value1
		value2 =intFloatCasting(two)
		print value2
		if isinstance(value1, str) or isinstance(value2, str):
			return "invalid values"
		else :
			value3=value1/value2
			value3=str(value3)
			return value3

@app.route('/mul', methods=['get'])
def create_cm2():
		one = request.args.get('one', None)
		two = request.args.get('two', None)
		value1 =intFloatCasting(one)
		print value1
		value2 =intFloatCasting(two)
		print value2
		if isinstance(value1, str) or isinstance(value2, str):
			return "invalid values"
		else :
			value3=value1*value2
			value3=str(value3)
			return value3

@app.route('/min', methods=['get'])
def create_cm3():
		one = request.args.get('one', None)
		two = request.args.get('two', None)
		value1 =intFloatCasting(one)
		print value1
		value2 =intFloatCasting(two)
		print value2
		if isinstance(value1, str) or isinstance(value2, str):
			return "invalid values"
		else :
			value3=value1-value2
			value3=str(value3)
			return value3





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
