# Overview on [FastAPI](https://fastapi.tiangolo.com)

[PDF version of the slides](https://whuss.github.io/fastapi_slides/slides.pdf)

## Installation instruction

The full example code referenced in the slides is in the [src](./src) directory.

Python version 3.8+ is required to run the examples.

For installation switch to the [src](./src) directory and run:

```bash
❯ make
```

The API can be started with:
```bash
❯ make run
```

Then point your browser to http://0.0.0.0:9001/docs to see the interactive api docs.

### Additional commands:

- `make test` for running the included tests
- `make fuzz` for fuzzing based on the generated OpenAPI schema.

## Building the slides

The slides are written in Markdown using [Marp](https://marp.app/).

For building the slides [node.js](https://nodejs.org/en/) is needed.

In the root directory first install [Marp](https://marp.app/) by running
```bash
❯ npm ci
```

Then build the html version of the slides with:

```bash
❯ npm run html
```

PDF and Powerpoint versions of the slides can be build using `npm run pdf` or `npm run html`.

