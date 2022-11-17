from Logger import Logger


logger = Logger()
logger.createLog(filename='log.md')
with open('logs/log.md', 'w') as file:
    file.write('```python\n')

