import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import RegisterTeam from './screens/RegisterTeam';
import TeamPanel from './screens/RegisterTeam';
import Home from './screens/home';

const Stack = createStackNavigator();

export default function App() {
    if (__DEV__) {
        console.log("starting in dev");
        global.url = "http://localhost:5000/"
    }else {
        console.log("starting in prod");
        global.url = "/"
    }
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen
                  name="Home"
                  component={Home}
                  options={{ title: 'Welcome' }}
                />
              <Stack.Screen name="RegisterTeam" component={RegisterTeam}  options={{ title: 'Registrar Equipo' }}/>
              <Stack.Screen name="TeamPanel" component={TeamPanel}  options={{ title: 'Panel de Equipo' }}/>
              </Stack.Navigator>
        </NavigationContainer>

    );
}


