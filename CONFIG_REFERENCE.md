# MiroFish Configuration Reference

## Environment Variables

All configuration is loaded from `.env` file in the project root directory.

### Core Configuration

#### `TEST_MODE` (Boolean)
- **Default**: `true` (for this setup)
- **Type**: String ("true" or "false")
- **Description**: Enables mock data generation instead of real API calls
- **Examples**:
  ```env
  TEST_MODE=true      # Use mock data, no API keys needed
  TEST_MODE=false     # Use real APIs, requires API keys
  ```

#### `FLASK_DEBUG` (Boolean)
- **Default**: `True`
- **Type**: String ("True" or "False")
- **Description**: Enables Flask debug mode for development
- **Effects**:
  - Auto-reload on file changes
  - Detailed error messages
  - Debug toolbar in browser
- **Examples**:
  ```env
  FLASK_DEBUG=True    # Development mode
  FLASK_DEBUG=False   # Production mode
  ```

#### `FLASK_HOST` (String)
- **Default**: `0.0.0.0`
- **Type**: String (IP address)
- **Description**: IP address to bind Flask server to
- **Examples**:
  ```env
  FLASK_HOST=0.0.0.0      # Listen on all interfaces
  FLASK_HOST=localhost    # Listen only locally
  FLASK_HOST=127.0.0.1    # Explicit localhost
  ```

#### `FLASK_PORT` (Integer)
- **Default**: `5001`
- **Type**: String (number)
- **Description**: Port for Flask backend server
- **Examples**:
  ```env
  FLASK_PORT=5001    # Default port
  FLASK_PORT=3000    # Alternative port
  FLASK_PORT=8000    # Another option
  ```

### LLM Configuration (Optional in Test Mode)

#### `LLM_API_KEY` (String)
- **Default**: Not set
- **Type**: String (API key)
- **Required When**: `TEST_MODE=false`
- **Description**: API key for LLM service
- **Providers Supported**:
  - OpenAI (prefix: `sk-`)
  - Aliyun DashScope (any format)
  - Any OpenAI-compatible API
- **Examples**:
  ```env
  LLM_API_KEY=sk-proj-xxxxx...    # OpenAI key
  LLM_API_KEY=sk-xxxxx...         # DashScope key
  ```

#### `LLM_BASE_URL` (String)
- **Default**: `https://api.openai.com/v1`
- **Type**: String (URL)
- **Description**: API endpoint for LLM service
- **Examples**:
  ```env
  # OpenAI
  LLM_BASE_URL=https://api.openai.com/v1
  
  # DashScope (Aliyun)
  LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
  
  # Local or custom
  LLM_BASE_URL=http://localhost:8000/v1
  ```

#### `LLM_MODEL_NAME` (String)
- **Default**: `gpt-4o-mini`
- **Type**: String (model identifier)
- **Description**: Model to use for LLM calls
- **Examples**:
  ```env
  # OpenAI models
  LLM_MODEL_NAME=gpt-4o-mini
  LLM_MODEL_NAME=gpt-4-turbo
  LLM_MODEL_NAME=gpt-3.5-turbo
  
  # DashScope models
  LLM_MODEL_NAME=qwen-plus
  LLM_MODEL_NAME=qwen-turbo
  LLM_MODEL_NAME=qwen-long
  ```

### Zep Configuration (Optional in Test Mode)

#### `ZEP_API_KEY` (String)
- **Default**: Not set
- **Type**: String (API key)
- **Required When**: `TEST_MODE=false`
- **Description**: API key for Zep memory graph service
- **Source**: https://app.getzep.com/
- **Examples**:
  ```env
  ZEP_API_KEY=your-zep-api-key-here
  ```

### OASIS Configuration

#### `OASIS_DEFAULT_MAX_ROUNDS` (Integer)
- **Default**: `10`
- **Type**: String (number)
- **Description**: Default maximum rounds for simulations
- **Examples**:
  ```env
  OASIS_DEFAULT_MAX_ROUNDS=10    # Short test
  OASIS_DEFAULT_MAX_ROUNDS=50    # Longer simulation
  OASIS_DEFAULT_MAX_ROUNDS=100   # Full test
  ```

#### `OASIS_SIMULATION_DATA_DIR` (String)
- **Default**: `backend/app/uploads/simulations/`
- **Type**: String (directory path)
- **Description**: Directory for storing simulation data
- **Auto-created**: Yes, if doesn't exist
- **Examples**:
  ```env
  # (Usually not needed to set, auto-configured)
  ```

### Report Agent Configuration

#### `REPORT_AGENT_MAX_TOOL_CALLS` (Integer)
- **Default**: `5`
- **Type**: String (number)
- **Description**: Maximum tool calls allowed per report generation
- **Examples**:
  ```env
  REPORT_AGENT_MAX_TOOL_CALLS=5    # Standard
  REPORT_AGENT_MAX_TOOL_CALLS=10   # More detailed
  REPORT_AGENT_MAX_TOOL_CALLS=3    # Quick reports
  ```

#### `REPORT_AGENT_MAX_REFLECTION_ROUNDS` (Integer)
- **Default**: `2`
- **Type**: String (number)
- **Description**: Maximum reflection rounds for report refinement
- **Examples**:
  ```env
  REPORT_AGENT_MAX_REFLECTION_ROUNDS=2    # Standard
  REPORT_AGENT_MAX_REFLECTION_ROUNDS=3    # More refinement
  REPORT_AGENT_MAX_REFLECTION_ROUNDS=1    # Quick
  ```

#### `REPORT_AGENT_TEMPERATURE` (Float)
- **Default**: `0.5`
- **Type**: String (decimal)
- **Range**: 0.0 to 1.0
- **Description**: Temperature for LLM sampling (creativity level)
- **Examples**:
  ```env
  REPORT_AGENT_TEMPERATURE=0.5    # Balanced
  REPORT_AGENT_TEMPERATURE=0.2    # More deterministic
  REPORT_AGENT_TEMPERATURE=0.8    # More creative
  ```

### Optional Boost Configuration

#### `LLM_BOOST_API_KEY` (String)
- **Default**: Not set
- **Type**: String (API key)
- **Optional**: Yes
- **Description**: Secondary LLM API key for faster responses
- **Only Used When**: Set explicitly
- **Examples**:
  ```env
  LLM_BOOST_API_KEY=sk-xxxxx...
  LLM_BOOST_BASE_URL=https://api.example.com/v1
  LLM_BOOST_MODEL_NAME=fast-model
  ```

---

## Current Default Configuration

The `.env` file currently contains:

```env
# ====== 测试模式配置 ======
TEST_MODE=true

# ====== LLM API配置
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

# ====== Flask配置 ======
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
```

### What This Means
- **Test Mode Active**: Application generates mock data
- **No API Keys Needed**: LLM_API_KEY and ZEP_API_KEY not required
- **Debug Mode On**: Full error reporting and auto-reload
- **Network Access**: Server accessible from all interfaces
- **Port 5001**: Backend server listens on port 5001

---

## Configuration Scenarios

### Scenario 1: Development with Test Data (Current)
```env
TEST_MODE=true
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
```
- Use for: Development, testing, demos
- API Keys: Not needed
- Speed: Instant
- Cost: Free

### Scenario 2: Production with Real APIs
```env
TEST_MODE=false
LLM_API_KEY=sk-xxxxx...
ZEP_API_KEY=your-zep-key...
FLASK_DEBUG=False
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
```
- Use for: Real data, production
- API Keys: Required
- Speed: API dependent
- Cost: Per API call

### Scenario 3: Local Testing
```env
TEST_MODE=true
FLASK_DEBUG=True
FLASK_HOST=127.0.0.1
FLASK_PORT=8000
```
- Use for: Local development only
- API Keys: Not needed
- Access: localhost only
- Port: 8000 instead of 5001

### Scenario 4: Mixed Mode
```env
TEST_MODE=false
LLM_API_KEY=sk-xxxxx...
ZEP_API_KEY=your-zep-key...
FLASK_DEBUG=True
```
- Use for: Real data with debug info
- API Keys: Required
- Useful for: Debugging real API issues

---

## Loading and Validation

### How Configuration Loads

1. **File Check**: Looks for `.env` in project root
2. **Default Values**: Uses hardcoded defaults if not found
3. **Override**: Environment variables override file values
4. **Type Conversion**: Converts strings to appropriate types
5. **Validation**: Checks required configs based on TEST_MODE

### Validation Rules

```python
# In test mode
if TEST_MODE=true:
    - All API keys optional
    - Application starts normally
    - All endpoints return mock data

# In real mode  
if TEST_MODE=false:
    - LLM_API_KEY required (raises error if missing)
    - ZEP_API_KEY required (raises error if missing)
    - Application requires valid API keys
```

### Error Messages

If configuration is invalid:
```
配置错误:
  - LLM_API_KEY 未配置 (可设置 TEST_MODE=true 使用虚拟数据测试)
  - ZEP_API_KEY 未配置 (可设置 TEST_MODE=true 使用虚拟数据测试)

请检查 .env 文件中的配置
```

---

## Advanced Configuration

### Custom Paths
```env
# Set custom upload directory
UPLOAD_FOLDER=/custom/path/uploads

# Set custom simulation directory
OASIS_SIMULATION_DATA_DIR=/custom/path/simulations
```

### Performance Tuning
```env
# Chunk size for document processing
DEFAULT_CHUNK_SIZE=1000    # Larger = fewer chunks

# Overlap for context preservation
DEFAULT_CHUNK_OVERLAP=100  # Larger = more context

# Max file size for uploads
MAX_CONTENT_LENGTH=104857600  # 100MB in bytes
```

### LLM Fine-tuning
```env
# For DashScope
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=2000

# For OpenAI
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL_NAME=gpt-4-turbo
LLM_TEMPERATURE=0.5
LLM_MAX_TOKENS=4000
```

---

## Configuration Precedence

Order from highest to lowest priority:
1. **Environment Variables** - `export KEY=value`
2. **.env File** - `.env` in project root
3. **Code Defaults** - `config.py` hardcoded defaults

Example:
```bash
# This overrides .env
export FLASK_PORT=9000
npm run dev

# This uses .env value
npm run dev
```

---

## Troubleshooting

### "API Key Missing" Error
```bash
# Check TEST_MODE status
grep TEST_MODE .env

# If TEST_MODE=false, add keys:
echo "LLM_API_KEY=your_key_here" >> .env
echo "ZEP_API_KEY=your_key_here" >> .env

# Then restart
npm run dev
```

### Port Already in Use
```bash
# Change port in .env
FLASK_PORT=5002

# Or use environment variable
FLASK_PORT=5002 npm run dev
```

### Configuration Not Loading
```bash
# Verify .env file exists
ls -la .env

# Check file format (no spaces around =)
cat .env

# Verify Python can read it
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('TEST_MODE'))"
```

---

## Best Practices

### Development
```env
TEST_MODE=true
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
```
- Enables mock data for faster development
- Auto-reload on changes
- Detailed error messages

### Testing
```env
TEST_MODE=true
FLASK_DEBUG=False
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
```
- Uses mock data
- Stable behavior
- Can run in CI/CD

### Production
```env
TEST_MODE=false
LLM_API_KEY=<from-secrets>
ZEP_API_KEY=<from-secrets>
FLASK_DEBUG=False
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
OASIS_DEFAULT_MAX_ROUNDS=50
```
- Uses real APIs
- Secure key management
- Optimized performance

---

## Quick Reference

| Variable | Test Mode | Real Mode | Type | Default |
|----------|-----------|-----------|------|---------|
| TEST_MODE | `true` | `false` | bool | false |
| LLM_API_KEY | optional | required | string | - |
| ZEP_API_KEY | optional | required | string | - |
| FLASK_DEBUG | True | False | bool | True |
| FLASK_PORT | 5001 | 5001 | int | 5001 |
| FLASK_HOST | 0.0.0.0 | 0.0.0.0 | string | 0.0.0.0 |

---

## Additional Resources

- `config.py` - Source code for configuration
- `.env` - Current configuration file
- `QUICK_START.md` - Getting started guide
- `TESTING_GUIDE.md` - Testing documentation
