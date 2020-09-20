import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import RegisterTeam from './screens/RegisterTeam';

const Stack = createStackNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen
                  name="Home"
                  component={RegisterTeam}
                  options={{ title: 'Welcome' }}
                />
              <Stack.Screen name="Profile" component={ProfileScreen} />
              </Stack.Navigator>

        </NavigationContainer>

    );
}



const ProfileScreen = () => {
  return <Text>This is Jane's profile</Text>;
};


