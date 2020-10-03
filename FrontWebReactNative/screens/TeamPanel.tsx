import { StatusBar } from 'expo-status-bar';
import React, {useState, useEffect} from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import globalStyles from '../styles/globalStyles';
import { get_team_api } from '../ApiCalls/get_team_api';

function render_team(json_team, navigation) {
    navigation.setOptions( {title: json_team.team_name + ' ' +json_team.id});
}

export default function TeamPanel( {route, navigation }) {
    const { value } = route.params;
    const [id, setId] = useState(JSON.stringify(value));

    const [json_team, setJson_team] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(
        () => {
            fetch('http://localhost:5000/team/'+id)
                .then((response) => response.json())
                .then((json) => setJson_team(json) )
                .catch((error) => console.log(error)  )
                .finally( () => setLoading(false) )
        }, [id]
    );

    useEffect (
        () => {
            render_team(json_team, navigation)
        }, [json_team]
    );



    return (  <View style={globalStyles.container}>
                <Text>hola {json_team.id}</Text>

              </View> );
};