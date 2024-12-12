from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
#from opentelemetry.sdk.metrics.export.controller import PushController

# Configuration du TracerProvider
# trace.set_tracer_provider(TracerProvider())
# tracer_provider = trace.get_tracer_provider()

# Configuration de l'exportateur OTLP
# otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
# span_processor = BatchSpanProcessor(otlp_exporter)
# tracer_provider.add_span_processor(span_processor)

# Configuration du fournisseur de métriques
# metrics.set_meter_provider(MeterProvider())
# meter = metrics.get_meter(__name__)

# Configuration de l'exportateur Prometheus
#exporter = PrometheusMetricReader()
#controller = PushController(meter, exporter, 5)

# Instrumentation de Django
#DjangoInstrumentor().instrument()