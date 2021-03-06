import { render, fireEvent } from '@testing-library/react-native';
import React from 'react';
import {  TextInput } from 'react-native';
import { RegisterTeam, RegisterTeam_with_function }   from '../screens/RegisterTeam';
import { get_url } from '../ApiCalls/utils'

test('Register team should have two texts and one button', () => {
    const { getAllByA11yLabel, getByText }  = render( <RegisterTeam /> );

    const team_name_input = getAllByA11yLabel('team-name');
    expect(team_name_input).toBeDefined();


    const submit_button = getByText('Crea tu equipo');
    expect(submit_button).toBeDefined();
});

test('Register team button should be executed with team name = A team and Name=Anibal', () => {

    const mockFn = jest.fn();

    const { getByText, getAllByA11yLabel, getByTestId }  = render( <RegisterTeam_with_function onSubmit={mockFn}/> );
    const submit_button = getByText('Crea tu equipo');
    const team_name_input = getByTestId('register_team_text_input');


    fireEvent.changeText(team_name_input,'A Team');


    fireEvent.press( submit_button );

    expect(mockFn).toHaveBeenCalledWith( "A Team", "", undefined);
});

test('Geting url in dev mode should return http://localhost:5000/ ', () => {
    expect(get_url()).toBe('http://localhost:5000/');
});
