![](http://i.imgur.com/LFYhXal.png)

This tool accepts a list of URL's from a file, parses each one, and converts the HTML to JSON format.

## Demo

Original HTML:
```html
<title>Buy Historical Stock Market Analytics JSON API | Stock Data API</title>
<meta name="description" content="Historical stock data JSON REST API for financial market data. Includes over
6,000 companies and more than 50 advanced technical indicators.">
```

Parsed JSON:
```json
{
  "tags": [
    {
      "attributes": null,
      "content": "Buy Historical Stock Market Analytics JSON API | Stock Data API",
      "name": "title"
    },
    {
      "attributes": {
        "content": "Historical stock data JSON REST API for financial market data. Includes over 6,000 companies
         and more than 50 advanced technical indicators.",
        "name": "description"
      },
      "content": null,
      "name": "meta"
    }
  ]
}
```