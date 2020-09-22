
import React from "react";
import { StyleSheet } from 'react-native';


const globalStyles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: '#fff',
        alignItems: 'flex-start'
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