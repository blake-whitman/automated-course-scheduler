# Dependencies
import config
import func
import time

# Login information
func.login(config.USERNAME, config.PASSWORD)

# Check if already registered and raise an exception if so
if func.isRegistered():
  print('ERROR: REGISTRATION FAILED --> You have already been registered for this specific lecture.')
  raise SystemExit(0)

# Register to your desired group
starttime = time.time()
tries = 1
while not func.isRegistered():
  print('Number of tries' %(str(tries)))
  func.register(config.DATE['day'], config.DATE['time'])
  time.sleep((config.INTERVAL * 60.0) - ((time.time() - starttime) % (config.INTERVAL * 60.0)))
  tries += 1

# Registration Complete
print('You have successfully registered for your desired lecture. Good luck in the course!' %(config.DATE['day'], config.DATE['time']))
