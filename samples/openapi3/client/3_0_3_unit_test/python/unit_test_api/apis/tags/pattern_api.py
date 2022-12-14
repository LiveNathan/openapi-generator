# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from unit_test_api.paths.request_body_post_pattern_is_not_anchored_request_body.post import PostPatternIsNotAnchoredRequestBody
from unit_test_api.paths.response_body_post_pattern_is_not_anchored_response_body_for_content_types.post import PostPatternIsNotAnchoredResponseBodyForContentTypes
from unit_test_api.paths.request_body_post_pattern_validation_request_body.post import PostPatternValidationRequestBody
from unit_test_api.paths.response_body_post_pattern_validation_response_body_for_content_types.post import PostPatternValidationResponseBodyForContentTypes


class PatternApi(
    PostPatternIsNotAnchoredRequestBody,
    PostPatternIsNotAnchoredResponseBodyForContentTypes,
    PostPatternValidationRequestBody,
    PostPatternValidationResponseBodyForContentTypes,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
