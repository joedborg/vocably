import cherrypy
from config import config
from questions import questions, answers


class Vocably(object):
    """
    A web application.
    """
    @cherrypy.expose
    def index(self):
        return open('static/html/index.html')

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def questions(self):
        """
        Serialize the list of questions to JSON.
        """
        return questions

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def answer(self, answer, question):
        """
        Check if the submitted answer is correct.
        This hides the correct answers from the front end.
        """
        if answer == answers[int(question)]:
            return {'correct': True}
        return {'correct': False}


if __name__ == '__main__':
    cherrypy.quickstart(Vocably(), '/', config=config)
