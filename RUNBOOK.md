# Operations Runbook

## Startup
1. Ensure Redis is running
2. Install dependencies
3. Start the application

## Health Checks
- App running
- Metrics endpoint reachable
- Redis connectivity

## Metrics to Monitor
- agent_requests_total
- agent_latency_seconds
- booking failures
- fallback invocations

## Common Issues

### Redis Down
- Agents continue stateless
- Session recovery unavailable

### Booking Failures
- Retry agent triggers
- Fallback agent escalates

## Restart Strategy
- Safe to restart (state stored in Redis)
