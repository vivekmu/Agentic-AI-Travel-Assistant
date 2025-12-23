# API Documentation

## Agent Interfaces

### Planner Agent
Input: goal (string)
Output: execution plan

### Flight Search Agent
Input: origin, destination, date
Output: list of flights

### Pricing Agent
Input: flight options
Output: selected flight

### Booking Agent
Input: approved flight
Output: booking confirmation

### Fallback Agent
Input: failed execution
Output: escalation record

## External APIs (Pluggable)
- Amadeus / Skyscanner (Flights)
- Razorpay / Stripe (Payments)
- Email / WhatsApp APIs