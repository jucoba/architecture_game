
import React from "react";
import { StyleSheet } from 'react-native';


const globalStyles = StyleSheet.create({
    mainContainer: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: '#fff',
        alignItems: 'flex-start'
    },
    titleContainer: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: '#fff',
        alignItems: 'flex-start'
    },
    fixedProperty: {
        flex: 1,
        flexDirection: 'row',
        backgroundColor: '#fff',
        alignItems: 'flex-start'
    },
    titleText: {
        fontSize:30,
    },
    textInupt: {
        borderColor: 'gray',
        borderWidth: 1,
        margin:5,
    },
    text: {
        margin:5,
    },

    button: {
        margin:5,
        alignItems: "center",
        backgroundColor: "#DDDDDD",
        padding: 10
    },
    link: {
        margin:5,
        padding: 10
    },
}
);

export default globalStyles