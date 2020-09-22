import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import RegisterTeam from './screens/RegisterTeam';
import Home from './screens/home';

const Stack = createStackNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen
                  name="Home"
                  component={Home}
                  options={{ title: 'Welcome' }}
                />
              <Stack.Screen name="RegisterTeam" component={RegisterTeam}  options={{ title: 'Registrar Equipo' }}/>
              </Stack.Navigator>
        </NavigationContainer>

    );
}


