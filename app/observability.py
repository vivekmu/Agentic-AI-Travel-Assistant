"""
Observability module for Agentic AI Travel Assistant

Provides:
- OpenTelemetry tracer
- Safe default configuration
- Console span export (local/dev friendly)
"""

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
    ConsoleSpanExporter,
)

# -------------------------------------------------
# Tracer Provider (global)
# -------------------------------------------------
provider = TracerProvider()

# -------------------------------------------------
# Span Processor (prints spans to console)
# -------------------------------------------------
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(span_processor)

# -------------------------------------------------
# Register provider globally
# -------------------------------------------------
trace.set_tracer_provider(provider)

# -------------------------------------------------
# Exported tracer (THIS IS WHAT YOUR CODE IMPORTS)
# -------------------------------------------------
tracer = trace.get_tracer("agentic-ai-travel-assistant")