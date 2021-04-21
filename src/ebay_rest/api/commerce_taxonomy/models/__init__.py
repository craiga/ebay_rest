# coding: utf-8

# flake8: noqa
"""
    Taxonomy API

    Use the Taxonomy API to discover the most appropriate eBay categories under which sellers can offer inventory items for sale, and the most likely categories under which buyers can browse or search for items to purchase. In addition, the Taxonomy API provides metadata about the required and recommended category aspects to include in listings, and also has two operations to retrieve parts compatibility information.  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from ...commerce_taxonomy.models.ancestor_reference import AncestorReference
from ...commerce_taxonomy.models.aspect import Aspect
from ...commerce_taxonomy.models.aspect_constraint import AspectConstraint
from ...commerce_taxonomy.models.aspect_metadata import AspectMetadata
from ...commerce_taxonomy.models.aspect_value import AspectValue
from ...commerce_taxonomy.models.base_category_tree import BaseCategoryTree
from ...commerce_taxonomy.models.category import Category
from ...commerce_taxonomy.models.category_aspect import CategoryAspect
from ...commerce_taxonomy.models.category_subtree import CategorySubtree
from ...commerce_taxonomy.models.category_suggestion import CategorySuggestion
from ...commerce_taxonomy.models.category_suggestion_response import CategorySuggestionResponse
from ...commerce_taxonomy.models.category_tree import CategoryTree
from ...commerce_taxonomy.models.category_tree_node import CategoryTreeNode
from ...commerce_taxonomy.models.compatibility_property import CompatibilityProperty
from ...commerce_taxonomy.models.compatibility_property_value import CompatibilityPropertyValue
from ...commerce_taxonomy.models.error import Error
from ...commerce_taxonomy.models.error_parameter import ErrorParameter
from ...commerce_taxonomy.models.get_categories_aspect_response import GetCategoriesAspectResponse
from ...commerce_taxonomy.models.get_compatibility_metadata_response import GetCompatibilityMetadataResponse
from ...commerce_taxonomy.models.get_compatibility_property_values_response import GetCompatibilityPropertyValuesResponse
from ...commerce_taxonomy.models.relevance_indicator import RelevanceIndicator
from ...commerce_taxonomy.models.value_constraint import ValueConstraint
