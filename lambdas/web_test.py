import random
def lambda_handler(event, context):
	number = random.random()
	table = """<html>
		<header><title>This is title</title></header>
		<body>
		THIS IS A TEST!!!
		</body>
		</html>"""
	table += '<th number=%S> </th>'
	return table