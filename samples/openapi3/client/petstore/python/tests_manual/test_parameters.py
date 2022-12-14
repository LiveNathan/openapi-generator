# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""
import unittest
import collections

from petstore_api import api_client, exceptions, schemas

from . import ParamTestCase


class TestParameter(unittest.TestCase):
    in_type_to_parameter_cls = {
        api_client.ParameterInType.PATH: api_client.PathParameter,
        api_client.ParameterInType.QUERY: api_client.QueryParameter,
        api_client.ParameterInType.COOKIE: api_client.CookieParameter,
        api_client.ParameterInType.HEADER: api_client.HeaderParameter,
    }

    invalid_inputs = (
        True,
        False
    )

    def test_throws_exception_when_schema_and_content_omitted(self):
        with self.assertRaises(ValueError):
            api_client.QueryParameter(
                name=''
            )

    def test_throws_exception_when_schema_and_content_input(self):
        with self.assertRaises(ValueError):
            schema = schemas.StrSchema
            api_client.QueryParameter(
                name='',
                schema=schema,
                content={'application/json': schema}
            )

    def test_succeeds_when_schema_or_content_input(self):
        schema = schemas.StrSchema
        api_client.QueryParameter(
            name='',
            schema=schema,
        )
        api_client.QueryParameter(
            name='',
            content={'application/json': schema}
        )

    def test_succeeds_and_fails_for_style_and_in_type_combos(self):
        style_to_in_type = {
            api_client.ParameterStyle.MATRIX: {api_client.ParameterInType.PATH},
            api_client.ParameterStyle.LABEL: {api_client.ParameterInType.PATH},
            api_client.ParameterStyle.FORM: {api_client.ParameterInType.QUERY, api_client.ParameterInType.COOKIE},
            api_client.ParameterStyle.SIMPLE: {api_client.ParameterInType.PATH, api_client.ParameterInType.HEADER},
            api_client.ParameterStyle.SPACE_DELIMITED: {api_client.ParameterInType.QUERY},
            api_client.ParameterStyle.PIPE_DELIMITED: {api_client.ParameterInType.QUERY},
            api_client.ParameterStyle.DEEP_OBJECT: {api_client.ParameterInType.QUERY},
        }
        schema = schemas.StrSchema
        for style in style_to_in_type:
            valid_in_types = style_to_in_type[style]
            for valid_in_type in valid_in_types:
                parameter_cls = self.in_type_to_parameter_cls[valid_in_type]
                parameter_cls(
                    name='',
                    style=style,
                    schema=schema,
                )
            invalid_in_types = {in_t for in_t in api_client.ParameterInType if in_t not in valid_in_types}
            for invalid_in_type in invalid_in_types:
                parameter_cls = self.in_type_to_parameter_cls[invalid_in_type]
                with self.assertRaises(ValueError):
                    parameter_cls(
                        name='',
                        style=style,
                        schema=schema,
                    )

    def test_throws_exception_when_invalid_name_input(self):
        disallowed_names = {'Accept', 'Content-Type', 'Authorization'}
        for disallowed_name in disallowed_names:
            with self.assertRaises(ValueError):
                api_client.HeaderParameter(
                    name=disallowed_name,
                    schema=schemas.StrSchema,
                )

    def test_query_style_form_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='?color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color='?color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='?color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='?color=hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='?color=')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='?color=blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='?color=blue&color=black&color=brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='?color=R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='?R=100&G=200&B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            parameter = api_client.QueryParameter(
                name=name,
                style=api_client.ParameterStyle.FORM,
                schema=schemas.AnyTypeSchema,
                explode=test_case.explode,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode in (True, False):
                    parameter = api_client.QueryParameter(
                        name=name,
                        style=api_client.ParameterStyle.FORM,
                        schema=schemas.AnyTypeSchema,
                        explode=explode,
                    )
                    parameter.serialize(invalid_input)

    def test_cookie_style_form_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color='color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='color=hello world')
            ),
            ParamTestCase(
                '',
                dict(color='color=')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='color=blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='color=blue&color=black&color=brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='color=R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R=100&G=200&B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            parameter = api_client.CookieParameter(
                name=name,
                style=api_client.ParameterStyle.FORM,
                schema=schemas.AnyTypeSchema,
                explode=test_case.explode,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode in (True, False):
                    parameter = api_client.CookieParameter(
                        name=name,
                        style=api_client.ParameterStyle.FORM,
                        schema=schemas.AnyTypeSchema,
                        explode=explode,
                    )
                    parameter.serialize(invalid_input)

    def test_style_simple_in_path_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R=100,G=200,B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            parameter = api_client.PathParameter(
                name=name,
                style=api_client.ParameterStyle.SIMPLE,
                schema=schemas.AnyTypeSchema,
                explode=test_case.explode,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode in (True, False):
                    parameter = api_client.PathParameter(
                        name=name,
                        style=api_client.ParameterStyle.SIMPLE,
                        schema=schemas.AnyTypeSchema,
                        explode=explode,
                    )
                    parameter.serialize(invalid_input)

    def test_style_simple_in_header_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R=100,G=200,B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            parameter = api_client.HeaderParameter(
                name=name,
                style=api_client.ParameterStyle.SIMPLE,
                schema=schemas.AnyTypeSchema,
                explode=test_case.explode,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode in (True, False):
                    parameter = api_client.HeaderParameter(
                        name=name,
                        style=api_client.ParameterStyle.SIMPLE,
                        schema=schemas.AnyTypeSchema,
                        explode=explode,
                    )
                    parameter.serialize(invalid_input)

    def test_style_label_in_path_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='.1')
            ),
            ParamTestCase(
                3.14,
                dict(color='.3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='.blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='.hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='.')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='.blue.black.brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='.blue.black.brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='.R.100.G.200.B.150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='.R=100.G=200.B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            parameter = api_client.PathParameter(
                name=name,
                style=api_client.ParameterStyle.LABEL,
                schema=schemas.AnyTypeSchema,
                explode=test_case.explode,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode in (True, False):
                    parameter = api_client.PathParameter(
                        name=name,
                        style=api_client.ParameterStyle.LABEL,
                        schema=schemas.AnyTypeSchema,
                        explode=explode,
                    )
                    parameter.serialize(invalid_input)

    def test_style_matrix_in_path_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color=';color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color=';color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color=';color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color=';color=hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color=';color')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color=';color=blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color=';color=blue;color=black;color=brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color=';color=R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color=';R=100;G=200;B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            parameter = api_client.PathParameter(
                name=name,
                style=api_client.ParameterStyle.MATRIX,
                schema=schemas.AnyTypeSchema,
                explode=test_case.explode,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode in (True, False):
                    parameter = api_client.PathParameter(
                        name=name,
                        style=api_client.ParameterStyle.MATRIX,
                        schema=schemas.AnyTypeSchema,
                        explode=explode,
                    )
                    parameter.serialize(invalid_input)

    def test_style_space_delimited_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue%20black%20brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R%20100%20G%20200%20B%20150')
            ),
        )
        for test_case in test_cases:
            parameter = api_client.QueryParameter(
                name=name,
                style=api_client.ParameterStyle.SPACE_DELIMITED,
                schema=schemas.AnyTypeSchema,
                explode=test_case.explode,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode in (True, False):
                    parameter = api_client.QueryParameter(
                        name=name,
                        style=api_client.ParameterStyle.SPACE_DELIMITED,
                        schema=schemas.AnyTypeSchema,
                        explode=explode,
                    )
                    parameter.serialize(invalid_input)

    def test_style_pipe_delimited_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue|black|brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R|100|G|200|B|150')
            ),
        )
        for test_case in test_cases:
            parameter = api_client.QueryParameter(
                name=name,
                style=api_client.ParameterStyle.PIPE_DELIMITED,
                schema=schemas.AnyTypeSchema,
                explode=test_case.explode,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode in (True, False):
                    parameter = api_client.QueryParameter(
                        name=name,
                        style=api_client.ParameterStyle.PIPE_DELIMITED,
                        schema=schemas.AnyTypeSchema,
                        explode=explode,
                    )
                    parameter.serialize(invalid_input)

    def test_path_params_no_style(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R,100,G,200,B,150')
            ),
        )
        for test_case in test_cases:
            parameter = api_client.PathParameter(
                name=name,
                schema=schemas.AnyTypeSchema,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                parameter = api_client.PathParameter(
                    name=name,
                    schema=schemas.AnyTypeSchema,
                )
                parameter.serialize(invalid_input)

    def test_header_params_no_style(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R,100,G,200,B,150')
            ),
        )
        for test_case in test_cases:
            parameter = api_client.HeaderParameter(
                name=name,
                schema=schemas.AnyTypeSchema,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                parameter = api_client.HeaderParameter(
                    name=name,
                    schema=schemas.AnyTypeSchema,
                )
                parameter.serialize(invalid_input)

    def test_query_params_no_style(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='?color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color='?color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='?color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='?color=hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='?color=')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='?color=blue&color=black&color=brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='?R=100&G=200&B=150')
            ),
        )
        for test_case in test_cases:
            parameter = api_client.QueryParameter(
                name=name,
                schema=schemas.AnyTypeSchema,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                parameter = api_client.QueryParameter(
                    name=name,
                    schema=schemas.AnyTypeSchema,
                )
                parameter.serialize(invalid_input)

    def test_cookie_params_no_style(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color='color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='color=hello world')
            ),
            ParamTestCase(
                '',
                dict(color='color=')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='color=blue&color=black&color=brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R=100&G=200&B=150')
            ),
        )
        for test_case in test_cases:
            parameter = api_client.CookieParameter(
                name=name,
                schema=schemas.AnyTypeSchema,
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                parameter = api_client.CookieParameter(
                    name=name,
                    schema=schemas.AnyTypeSchema,
                )
                parameter.serialize(invalid_input)

    def test_checks_content_lengths(self):
        with self.assertRaises(ValueError):
            api_client.QueryParameter(
                name='', content={}
            )
        with self.assertRaises(ValueError):
            api_client.QueryParameter(
                name='',
                content={'application/json': schemas.AnyTypeSchema, 'text/plain': schemas.AnyTypeSchema}
            )
        # valid length works
        api_client.QueryParameter(
            name='',
            content={'application/json': schemas.AnyTypeSchema}
        )

    def test_header_content_json_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                {'color': 'null'}
            ),
            ParamTestCase(
                1,
                {'color': '1'}
            ),
            ParamTestCase(
                3.14,
                {'color': '3.14'}
            ),
            ParamTestCase(
                'blue',
                {'color': '"blue"'}
            ),
            ParamTestCase(
                'hello world',
                {'color': '"hello world"'}
            ),
            ParamTestCase(
                '',
                {'color': '""'}
            ),
            ParamTestCase(
                True,
                {'color': 'true'}
            ),
            ParamTestCase(
                False,
                {'color': 'false'}
            ),
            ParamTestCase(
                [],
                {'color': '[]'}
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                {'color': '["blue", "black", "brown"]'}
            ),
            ParamTestCase(
                {},
                {'color': '{}'}
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                {'color': '{"R": 100, "G": 200, "B": 150}'}
            ),
        )
        for test_case in test_cases:
            parameter = api_client.HeaderParameter(
                name=name,
                content={'application/json': schemas.AnyTypeSchema}
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

    def test_query_content_json_serialization(self):
        name = 'color'
        test_cases = (
            ParamTestCase(
                None,
                {'color': '?color=null'}
            ),
            ParamTestCase(
                1,
                {'color': '?color=1'}
            ),
            ParamTestCase(
                3.14,
                {'color': '?color=3.14'}
            ),
            ParamTestCase(
                'blue',
                {'color': '?color=%22blue%22'}
            ),
            ParamTestCase(
                'hello world',
                {'color': '?color=%22hello%20world%22'}
            ),
            ParamTestCase(
                '',
                {'color': '?color=%22%22'}
            ),
            ParamTestCase(
                True,
                {'color': '?color=true'}
            ),
            ParamTestCase(
                False,
                {'color': '?color=false'}
            ),
            ParamTestCase(
                [],
                {'color': '?color=%5B%5D'}
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                {'color': '?color=%5B%22blue%22%2C%22black%22%2C%22brown%22%5D'}
            ),
            ParamTestCase(
                {},
                {'color': '?color=%7B%7D'}
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                {'color': '?color=%7B%22R%22%3A100%2C%22G%22%3A200%2C%22B%22%3A150%7D'}
            ),
        )
        for test_case in test_cases:
            parameter = api_client.QueryParameter(
                name=name,
                content={'application/json': schemas.AnyTypeSchema}
            )
            serialization = parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

    def test_throws_error_for_unimplemented_serialization(self):
        with self.assertRaises(NotImplementedError):
            parameter = api_client.HeaderParameter(
                name='color',
                content={'text/plain': schemas.AnyTypeSchema}
            )
            parameter.serialize(None)


if __name__ == '__main__':
    unittest.main()
