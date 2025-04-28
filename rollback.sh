#!/bin/bash

# Simple rollback script for the blue/green deployment

# Get current active environment
CURRENT_ENV=$(cat deploy/active_env.txt)

# Determine environment to roll back to
if [ "$CURRENT_ENV" == "blue" ]; then
    ROLLBACK_ENV="green"
else
    ROLLBACK_ENV="blue"
fi

echo "Rolling back from $CURRENT_ENV to $ROLLBACK_ENV environment..."

# Update active environment
echo $ROLLBACK_ENV > deploy/active_env.txt

echo "Rollback complete. Active environment is now: $ROLLBACK_ENV"
echo "You would need to restart the application in the $ROLLBACK_ENV environment to complete the rollback." 