
def pytest_runtest_call(__multicall__):
    try:
        __multicall__.execute()
    except KeyboardInterrupt as e:
        raise e
    except AssertionError as e:
        from framework.logger import framework_logger
        if framework_logger:
            framework_logger.exception('Assert in test:')
        raise e
    except Exception as e:
        from framework.logger import framework_logger
        if framework_logger:
            framework_logger.exception('Exception in test:')
        raise e