# Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
    *variable declaration

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
   1. use dict.get('c')
   2. using exception handling

- What is a unit test?  
    *It is the testing of individual methods and functions in an app.

- What is an integration test?  
    *It is testing 2 more methods or functions together.

- What is the role of web application framework, like Flask?  
  *A framework is a library of functions and methods that allows us to define how to respond to requests and which requests to respond to.
- You can pass information to Flask either as a parameter in a route URL  
  (like '/foods/pretzel') or using a URL query param  (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?  
    *Query params are used when there are forms involved to collect a user's input.

- How do you collect data from a URL placeholder parameter using Flask?  
  @app.route('/home/<`int: page_num`>')
  def homepage(page_num):
      ...

- How do you collect data from the query string using Flask?  
    Using the request method:  
    if query string = foods?type=pretzel, key,value pair is {'type': 'pretzel'}  
    `type = request.args['type']`

- How do you collect data from the body of the request using Flask?  

- What is a cookie and what kinds of things are they commonly used for?
    cookies are a way to store a state of an app on the client. The information stored in cookies in the form of string/value pair allows the client to remember important information for a better user experience.  

- What is the session object in Flask?  
    It is a special dictionary that contains information in key/value pairs, and is encrypted to the client.

- What does Flask's `jsonify()` do?  
  It allows us to return a JSON obj.
  