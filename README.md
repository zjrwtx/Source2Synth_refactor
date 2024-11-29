# Multi-Hop QA Dataset Generator

A powerful tool for generating high-quality multi-hop question answering datasets using AI models and sophisticated data processing techniques.

## Features

- **AI-Powered Generation**: Leverages DeepSeek's language models for creating complex, multi-step reasoning questions
- **Multi-Hop Reasoning**: Generates QA pairs that require multiple steps of logical reasoning
- **Quality Control**: Implements comprehensive quality filters and complexity metrics
- **Flexible Processing**: Supports both single text and batch processing
- **Detailed Output**: Includes reasoning steps, supporting facts, and metadata

## Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/zjrwtx/Source2Synth_refactor.git
cd Source2Synth_refactor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file in the root directory with the following content:
```env
OPENAI_COMPATIBILIY_API_BASE_URL=your_api_base_url
OPENAI_COMPATIBILIY_API_KEY=your_api_key
```

## Usage

### Basic Usage

```python
from data_processor import ProcessorConfig, UserDataProcessor

# Create configuration
config = ProcessorConfig(
    seed=42,
    min_length=50,
    max_length=1000,
    quality_threshold=0.7,
    complexity_threshold=0.5,
    dataset_size=10,
    use_ai_model=True,
    model_temperature=0.4,
    max_tokens=4096
)

# Initialize processor
processor = UserDataProcessor(config)

# Process single text
text = """
The invention of transistors revolutionized electronics in the 1950s. 
These tiny semiconductor devices enabled the development of smaller and more 
efficient computers. The miniaturization of computers led to the creation of 
personal computers in the 1980s.
"""

result = processor.process_text(text, source="technology_article")
```

### Batch Processing

```python
# Process multiple texts
texts = [
    "Text about technology...",
    "Text about environment...",
    "Text about medicine..."
]

results = processor.process_batch(texts, sources=["tech", "env", "med"])
```

## Output Format

The generator produces structured output in the following format:

```json
{
    "text": "Original text content",
    "qa_pairs": [
        {
            "question": "Complex multi-hop question",
            "reasoning_steps": [
                "First reasoning step",
                "Second reasoning step",
                "Final reasoning step"
            ],
            "answer": "Comprehensive answer",
            "supporting_facts": [
                "Supporting fact 1",
                "Supporting fact 2"
            ],
            "type": "multi_hop_qa"
        }
    ],
    "metadata": {
        "source": "Source identifier",
        "timestamp": "Generation time",
        "complexity": 0.85
    }
}
```

## Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| seed | Random seed for reproducibility | 42 |
| min_length | Minimum text length | 50 |
| max_length | Maximum text length | 512 |
| quality_threshold | Minimum quality score | 0.7 |
| complexity_threshold | Minimum complexity score | 0.5 |
| dataset_size | Target dataset size | 1000 |
| use_ai_model | Whether to use AI model | True |
| model_temperature | AI model temperature | 0.4 |
| max_tokens | Maximum tokens for AI model | 4096 |

## Quality Metrics

The generator employs several quality metrics:

1. **Text Quality**
   - Minimum length requirements
   - Special character ratio checks
   - Sentence structure analysis

2. **Question Complexity**
   - Number of reasoning steps
   - Supporting facts count
   - Question and answer length
   - Reasoning chain coherence

3. **Overall Complexity Score**
   - Weighted combination of multiple factors
   - Normalized to 0-1 range
   - Configurable thresholds

## Running Tests

The project includes comprehensive tests:

```bash
python test_example.py
```

This will:
- Generate sample QA pairs
- Save results to JSON files
- Display detailed statistics
- Analyze generation quality

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.



## Acknowledgments

- DeepSeek for providing the language model API
- All contributors and users of this project
Reference since the improvement from: https://github.com/sanowl/Source2Synth
## Contact

For questions and feedback, please open an issue in the GitHub repository. 
