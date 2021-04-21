# coding: utf-8

# flake8: noqa
"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from ...sell_metadata.models.automotive_parts_compatibility_policy import AutomotivePartsCompatibilityPolicy
from ...sell_metadata.models.automotive_parts_compatibility_policy_response import AutomotivePartsCompatibilityPolicyResponse
from ...sell_metadata.models.error import Error
from ...sell_metadata.models.error_parameter import ErrorParameter
from ...sell_metadata.models.exclusion import Exclusion
from ...sell_metadata.models.item_condition import ItemCondition
from ...sell_metadata.models.item_condition_policy import ItemConditionPolicy
from ...sell_metadata.models.item_condition_policy_response import ItemConditionPolicyResponse
from ...sell_metadata.models.listing_structure_policy import ListingStructurePolicy
from ...sell_metadata.models.listing_structure_policy_response import ListingStructurePolicyResponse
from ...sell_metadata.models.negotiated_price_policy import NegotiatedPricePolicy
from ...sell_metadata.models.negotiated_price_policy_response import NegotiatedPricePolicyResponse
from ...sell_metadata.models.product_adoption_policy import ProductAdoptionPolicy
from ...sell_metadata.models.product_adoption_policy_response import ProductAdoptionPolicyResponse
from ...sell_metadata.models.return_policy import ReturnPolicy
from ...sell_metadata.models.return_policy_details import ReturnPolicyDetails
from ...sell_metadata.models.return_policy_response import ReturnPolicyResponse
from ...sell_metadata.models.sales_tax_jurisdiction import SalesTaxJurisdiction
from ...sell_metadata.models.sales_tax_jurisdictions import SalesTaxJurisdictions
from ...sell_metadata.models.time_duration import TimeDuration
