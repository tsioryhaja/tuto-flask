from flask import Flask, render_template
from datetime import date
app = Flask(__name__)

class Test():
	def test(self):
		return 'test'
	@staticmethod
	def static_test():
		return 'ttttt'


class TestController():
	@staticmethod
	@app.route('/action')
	def test_index():
		return dict(test='test',data='test')
		

@app.route('/')
def index():
	return render_template('acceuil.html', titre='test', date=date.today, text=Test.static_test())

if __name__ == '__main__':
	app.run()