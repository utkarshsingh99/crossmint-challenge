## Crossmint Coding Challenge

Hi!

This is my submission to Crossmint's coding challenge. 
As mentioned in the requirements, the code has been kept as modularized and structured as possible,  
devoid of duplication and replete with abstractions.

The application code has 3 aspects:
1. API Client
2. Megaverse Map
3. Astral Objects

### API Client

All the interfacing with the crossmint challenge URL is done through this class. It is the responsibility of this class to make POST, DELETE or GET requests to the provided API. A separate Config class is created to store user defined variables, synonymous with environment variables. 

##### Bypassing rate limits of the API
Since the challenge API is rate limited, the application will try polling the API with a fixed number of tries after a fixed interval. This will be done for all the requests.

##### Avoiding duplication and extending the use case
The logic to retry sending the same request to the API will be used for all the different methods. Hence, a separate utility function is called by all three methods.

### Megaverse Map

##### Fetch the required grid
Using the goal API, the application fetches the requirements to build the map.

##### Create map
Each element (except "SPACE") in the grid provided by the goal API is passed to the Astral Object Factory to create a new polyanet, cometh or soloon.

##### Delete map
A simple function that was used for my own testing. It is not needed to accomplish the requirements, but I included it for exhaustive purposes.

### Astral Object Factory

##### Classify objects
The object factory class simply identifies the category of the astral object (polyanet, cometh or soloon) and the properties (direction, color).

##### Astral Object
An abstract class is created to serve as the blueprint for different astract objects. Common functionalities like create, delete are implemented here and additional specifications (such as endpoints, color or direction) are provided in the individual declarations of the classes which inherit the abstract base class.

#### Inclusion of logging

Additionally, I have also implemented logging in the application and committed the `.log` file for exhaustive purposes.

#### Exclusion of testing
I wanted to include tests in the application but the goal API itself is not working anymore once I have successfully validated my submission. For this reason, and to not overdo the solution, I have chosed to not include unit tests in the application.
If we wanted to do it, we could randomly generate grid data and test each class' functionality individually using `pytest`. 
