### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Python is a backend language that typically runs server side and is often used in other application development less limited to web development only.
  JavaScript is known to be a more browser based frontend language that runs client side 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  - Can utilize error first handling
    - If the value is not None, get the value.
    - Use a try/except block that accounts for is the key of "c" is not found.

- What is a unit test?
  Unit test focus more on the testing individual modules and functions and if they will perform as expected.

- What is an integration test?
  Integration testing involves mixing different components to see if they work together.

- What is the role of web application framework, like Flask?
  A framework like flask allows for building of fullstack application of the frontend browser based portion of our application along with the server side and a database.  Flask via python help with development of the applications interface.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  Querying would be best for working with a database to retrieve certain values, while a url route would work better in rendering prewriten pages.

- How do you collect data from a URL placeholder parameter using Flask?
  Flask will if told to interpret the values in the delimiter.

- How do you collect data from the query string using Flask?
  We assign the query to be collected from the request.args

- How do you collect data from the body of the request using Flask?
  We assign the data to be collected from the request.from

- What is a cookie and what kinds of things are they commonly used for?
  Cookies are sent from the server to browser as a sort of token.
  It can be used for session management, authentication and tracking.

- What is the session object in Flask?
  The session object if a open window/tab way to handle is used to prevent tampering.  A way to validate that data is only being sent to and from the server and client and not intersected or manipulated by a third parties.  

- What does Flask's `jsonify()` do?
  Is a module that can be imported to convert items into json.
  Useful for messages and JSON based browser storage.
