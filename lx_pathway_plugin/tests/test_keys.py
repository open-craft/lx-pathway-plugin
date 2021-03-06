"""
Test for the LabXchange pathway learning context opaque keys
"""
from unittest import TestCase

from opaque_keys.edx.keys import LearningContextKey, UsageKey

from lx_pathway_plugin.keys import PathwayLocator, PathwayUsageLocator


class PathwayKeyTests(TestCase):
    """
    Test for the LabXchange pathway learning context REST API
    """

    def test_pathway_key_parsing(self):
        """
        Test parsing of pathway keys
        """
        key_str = 'lx-pathway:00000000-e4fe-47af-8ff6-123456789000'
        key = LearningContextKey.from_string(key_str)
        self.assertEqual(str(key), key_str)
        self.assertIsInstance(key, PathwayLocator)

    def test_usage_key_parsing(self):
        """
        Test parsing of pathway usage keys
        """
        parent_key = LearningContextKey.from_string('lx-pathway:00000000-e4fe-47af-8ff6-123456789000')
        # Key of a normal top-level block in a pathway:
        key_str = 'lx-pb:00000000-e4fe-47af-8ff6-123456789000:unit:0ff24589'
        key = UsageKey.from_string(key_str)
        self.assertEqual(str(key), key_str)
        self.assertIsInstance(key, PathwayUsageLocator)
        self.assertEqual(key.context_key, parent_key)
        self.assertEqual(key, UsageKey.from_string(key_str))  # self equality
        # Key of a child block in a pathway:
        key_str = 'lx-pb:00000000-e4fe-47af-8ff6-123456789000:problem:0ff24589:1-2'
        key = UsageKey.from_string(key_str)
        self.assertEqual(str(key), key_str)
        self.assertIsInstance(key, PathwayUsageLocator)
        self.assertEqual(key.context_key, parent_key)
        self.assertEqual(key, UsageKey.from_string(key_str))  # self equality
        self.assertNotEqual(
            UsageKey.from_string('lx-pb:00000000-e4fe-47af-8ff6-123456789000:unit:0ff24589'),
            UsageKey.from_string('lx-pb:00000000-e4fe-47af-8ff6-123456789000:unit:0ff24589:1-2'),
        )
