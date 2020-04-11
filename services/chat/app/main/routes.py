# from flask import session, redirect, url_for, render_template, request, Blueprint, jsonify
# from . import main
# from .forms import LoginForm
# from flask_restful import Resource, Api

# main_blueprint = Blueprint("main", __name__, template_folder='../templates', static_folder='../templates')


# @main.route('/', methods=['GET', 'POST'])
# def index():
#     """Login form to enter a room."""
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         session['room'] = form.room.data
        
#         return redirect(url_for('.chat'))
#     elif request.method == 'GET':
#         form.name.data = session.get('name', '')
#         form.room.data = session.get('room', '')

#     return render_template('index.html', form=form)

# @main.route('/chat')
# def chat():
#     """Chat room. The user's name and room must be stored in
#     the session."""
#     name = session.get('name', '')
#     room = session.get('room', '')
#     if name == '' or room == '':
#        return redirect(url_for('.index'))
#     # return jsonify({
#     #     'name':name,
#     #     'message':room,
#     #     'people':['teo','dad','isi']

#     # })
#     return render_template('chat.html', name=name, room=room)


# @main.route('/chat/ping', methods=['GET'])
# def ping_pong():
#     return jsonify({
        
#         "items": [
#             { "id": 1, "name": "Apples",  "price": "$2" },
#             { "id": 2, "name": "Peaches", "price": "$5" }
#         ] 

#     })