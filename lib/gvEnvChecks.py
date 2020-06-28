"""
Validate the environmental support systems.

These tests ensure that the proper environment for testing has been setup. It
eliminates the need to provide mock objects for environmental support,
including logging when running unit tests since these tests provide a sanity
check for the for the environmental support systems.
system..

.. only:: development_administrator

    Created on Jun. 24, 2020
    
    @author: Jonathan Gossage
"""

import inspect
import logging
from typing import Sequence
import unittest

import lib.gvLogging

_logger = None


def setUpModule():
    # Sets up a preliminary logging environment
    global _logger
    _logger = lib.gvLogging.setLogging(propogate=False)


def teardownModule():
    logging.shutdown()


class TestEnvironment(unittest.TestCase):

    def testLogging(self):
        """
Logging tester

Test that logging works properly even when the Global Village logger has not
been installed. This is done by trying to log a message and seeing that the
logging attempt was detected. This is essentially an integration test that
should pass before running any other tests as the entire environment relies on
logging and mock objects for logging are a nuisance for unit test logging and a
no-no for integration testing. Since this test is an integration test, it makes
no attempt to completely test the logging functionality. It simply provides a
quick check that important logger functionality is working properly.
        """
        _levels = (logging.DEBUG, logging.INFO, logging.WARNING,
                   logging.ERROR, logging.CRITICAL)

        def _checkmsg(self) -> Sequence[str]:
            """
Encapsulates the generation of logging messages.
            """
            # Gives a list of the members in the Logging class we are using
            _lf = inspect.getmembers(_logger,
                                     predicate=inspect.ismethod)
            # we start with a list of tuples containing the name of an instance
            # method - k  and a copy of the method instance - v
            # We end up with a dictionary where the key is k and the value is v
            # for each entry in the dictionary.
            _lfd = {k: v for k, v in _lf}
            del(_lf)  # Get rid of any references to stack frames
            _msg = []  # Will contain the test messages to be logged
            # Loop logging a test message for each logging level. Messages that
            # have a logging level that is greater than the message level
            # should not show up when the results of the logging are tested
            for i, _lv in enumerate(_levels):
                _ln = logging.getLevelName(_levels[i]).lower()
                _msg.append(
                    f'test {_ln} message for {self.testLogging.__name__}')
                # Log the message if the logging level allows it
                # We pick up the logging method from the dictionary _lfd
                # We then call the method so defined to do the actual logging.
                assert len(_msg) > 0
                _lfd[_ln](_msg[-1])
            return _msg

        # Continue with definition of testLogging method
        self.assertTrue(_logger is not None)
        self.assertIsInstance(_logger, logging.Logger)
        _hh = _logger.hasHandlers()
        _tl = _logger.getEffectiveLevel()
        _ln = logging.getLevelName(_tl)
        self.assertGreaterEqual(_tl,
                                logging.INFO)

        with self.assertLogs(_logger,
                             logging.WARNING) as _al:
            _msg = _checkmsg(self)
        # Now we can verify the messages by looping through the logged
        # messages and verifying that all messages got logged correctly
        _oc = 0
        # Loop through the logging levels that we are testing
        # We want to verify that all messages that should have been logged
        # did get logged and that messages that should not have been logged
        # were ignored
        for i in range(len(_msg)):
            _lv = _levels[i]  # Get the level we are testing
            _ltn = logging.getLevelName(_lv)
            if _tl <= _lv:
                # Now validate that the message has been logged
                # Check that the logging level was correctly set
                _m = _al.output[_oc]  # Get the logged message
                self.assertTrue(_ltn in _m,
                                f'LTN is {_ltn} and MSG is {_m}')
                # Check that the original log message is in the logged
                # message
                self.assertTrue(_msg[i] in _m)
                _oc += 1  # Count the logged messages
            else:  # This message should not have been logged
                # Loop through the output making sure that no message has been
                # logged for a suppressed logging level which we are now
                # handling.
                for i in range(len(_al.output) - _levels.index(_tl),
                               len(_al.output)):
                    self.assertFalse(_ltn in _al.output[i],
                                     f'LTN is {_ltn} and'
                                     f' MSG is {_al.output[i]}')

            # Test the logging of exceptions
            _exmsg = 'We got an Assertion exception'
            with self.assertLogs(_logger, logging.WARNING) as _bl:
                try:
                    raise AssertionError('Testing the logging of exceptions')
                except AssertionError:
                    _logger.exception(_exmsg)
            self.assertTrue(_exmsg in _bl.output[0],
                            f'expected msg - {_exmsg},'
                            f' actual msg - {_bl.output[0]}')


if __name__ == '__main__':
    unittest.main()
