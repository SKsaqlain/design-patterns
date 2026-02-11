import asyncio
import logging
from broker import WeatherBroker
from producer import TemperatureProducer
from consumer import WeatherAppConsumer

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-10s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

async def main():
    logger.info("=== Observer Pattern — Weather Broker Example ===")

    # Set up the broker and create a topic
    weather_broker=WeatherBroker(broker_name='weather_broker')
    await weather_broker.create_topic('temperature_topic')

    # Create a producer and register it with the broker's topic
    temp_producer=TemperatureProducer(producer_name='temp_producer')
    await temp_producer.register_with_topic(broker=weather_broker,topic='temperature_topic')

    # Create consumers (observers) that will receive temperature updates
    weather_app=WeatherAppConsumer(name='weather_app',topic='temperature_topic')
    news_app=WeatherAppConsumer(name='news_app',topic='temperature_topic')

    # Subscribe consumers to the topic via the broker
    await weather_broker.subscribe(weather_app,topic='temperature_topic')
    await weather_broker.subscribe(news_app,topic='temperature_topic')

    # Produce messages — each one broadcasts to all subscribed consumers
    await temp_producer.produce("'{'temperature: 15, mesaurement: C'}'")
    await temp_producer.produce("'{'temperature: 16, mesaurement: C'}'")
    await temp_producer.produce("'{'temperature: 17, mesaurement: C'}'")









if __name__=='__main__':
    # main()
    asyncio.run(main())