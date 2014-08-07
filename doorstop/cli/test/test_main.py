"""Unit tests for the doorstop.cli.main module."""

import unittest
from unittest.mock import patch, Mock

from doorstop.cli import main


class TestMain(unittest.TestCase):

    """Unit tests for the `main` function."""  # pylint: disable=R0201

    @patch('doorstop.cli.commands.get')
    def test_run(self, mock_get):
        """Verify the main CLI function can be called."""
        main.main(args=[])
        mock_get.assert_called_once_with(None)

    @patch('doorstop.cli.main.gui')
    def test_gui(self, mock_gui):
        """Verify the GUI function can be called."""
        main.main(args=['--gui'])
        mock_gui.assert_called_once()

    @patch('doorstop.cli.main.server')
    def test_server(self, mock_server):
        """Verify the server function can be called."""
        main.main(args=['--serve'])
        mock_server.assert_called_once()

    @patch('doorstop.cli.commands.run', Mock(side_effect=KeyboardInterrupt))
    def test_interrupt(self):
        """Verify the CLI can be interrupted."""
        self.assertRaises(SystemExit, main.main, [])
