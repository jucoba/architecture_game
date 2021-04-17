# architecture_game
A game to tech evolutive architecture

on dev mode needs in a web enviroment needs a plugin to allow CORS. I used Allow CORS: Access-Control-Allow-origin (https://mybrowseraddon.com/access-control-allow-origin.html)

##Install
npm install
pip install numpy

##set Vitual env
source venv/bin/activate

##Testing
Using React Native Test Library (https://callstack.github.io/react-native-testing-library/docs/getting-started)

##Run de front server
cd FrontWebReactNative
expo start

##Run the backend server
cd FlaskServer
./start_server.sh

Inside FrontWebReactNative
1. Install React Native Test Library
npm install --save-dev @testing-library/react-native 

2. Install react-test-renderer
npm install react-test-renderer

3. Install jest
npm install --save-dev jest
