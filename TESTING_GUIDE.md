# MiroFish Testing Guide

## Quick Start - Test Mode (No API Keys Required)

The project is now configured to run in **TEST_MODE**, which allows you to test the application without requiring any external API keys.

### Environment Configuration

The `.env` file has been created with `TEST_MODE=true`. This enables:

- **Mock Data Generation**: All APIs return simulated data instead of calling real services
- **No API Keys Required**: LLM and Zep API keys are optional
- **Full Feature Testing**: Test all features with realistic dummy data

### What's Included in Test Mode

#### 1. **Entity Generation**
- Mock graph entities with realistic names, types, and relationships
- Supports multiple entity types: Student, PublicFigure, Organization, Location, Topic
- Generates edges/relationships between entities

#### 2. **Profile Generation**
- Reddit profiles with personality and behavior descriptors
- Twitter profiles with engagement levels
- Realistic user patterns for simulation testing

#### 3. **Simulation Configuration**
- Mock OASIS simulation configs with configurable rounds
- Platform settings (Reddit, Twitter)
- Interaction parameters and probabilities

#### 4. **Task Management**
- Task status tracking with mock progress
- Completion timestamps and status updates

### Running the Application

#### Backend Only (Python Flask):
```bash
cd backend
python run.py
# Server will run on http://localhost:5001
```

#### Frontend Only (Vue.js):
```bash
cd frontend
npm run dev
# Server will run on http://localhost:5173
```

#### Both Together:
```bash
npm run dev
# Runs both backend and frontend concurrently
```

### API Endpoints for Testing

#### Get Graph Entities
```bash
curl http://localhost:5001/api/simulation/entities/test_graph_123
```

Response (mock data):
```json
{
  "success": true,
  "data": {
    "graph_id": "test_graph_123",
    "filtered_count": 10,
    "entity_types": ["Student", "PublicFigure", "Organization"],
    "entities": [
      {
        "id": "entity_xxx",
        "name": "Alice Johnson",
        "type": "Student",
        "description": "Mock Student entity for testing purposes",
        "properties": {...}
      }
    ],
    "edges": [...]
  }
}
```

#### Get Entities by Type
```bash
curl http://localhost:5001/api/simulation/entities/test_graph_123/by-type/Student
```

#### Get Single Entity Detail
```bash
curl http://localhost:5001/api/simulation/entities/test_graph_123/entity_abc123
```

### Using Real APIs (Optional)

To use real APIs instead of test mode, either:

1. **Option A**: Add API keys to `.env` and set `TEST_MODE=false`
   ```env
   TEST_MODE=false
   LLM_API_KEY=your_real_key_here
   ZEP_API_KEY=your_real_zep_key_here
   ```

2. **Option B**: Remove the TEST_MODE variable entirely
   ```env
   # .env without TEST_MODE defaults to false
   LLM_API_KEY=your_real_key_here
   ZEP_API_KEY=your_real_zep_key_here
   ```

### Testing Features

#### Test Entity Filtering
```bash
# Filter by specific entity types
curl "http://localhost:5001/api/simulation/entities/test_graph_123?entity_types=Student,PublicFigure"
```

#### Test Profile Generation
The test data generator creates realistic profiles for:
- Reddit simulation with personality traits and posting frequency
- Twitter simulation with engagement levels and handle formats
- Configurable counts and entity associations

#### Test Simulation Config
Mock configs include:
- Simulation ID and name
- Max rounds (default: 10)
- Platform configurations
- Realistic parameter values

### File Structure

New test files created:
- `/backend/app/services/test_data_generator.py` - Mock data generation utilities
- `/.env` - Configuration file with TEST_MODE=true

Modified files for test support:
- `/backend/app/config.py` - Added TEST_MODE config option
- `/backend/app/api/simulation.py` - Added test mode handling to API endpoints

### How Test Mode Works

1. **Configuration Check**: Each API endpoint checks if `Config.TEST_MODE` is True
2. **Mock Data Generation**: If in test mode, generates realistic mock data using TestDataGenerator
3. **Real API Fallback**: If test mode is disabled, attempts to use real LLM/Zep APIs
4. **Error Handling**: Graceful fallback with appropriate error messages

### Debugging Test Data

To customize mock data generation, edit `/backend/app/services/test_data_generator.py`:

```python
# Change the number of entities generated
TestDataGenerator.generate_entities(count=20)

# Customize entity types
TestDataGenerator.generate_entities(
    count=10, 
    entity_types=["Student", "Organization"]
)

# Modify profile generation
TestDataGenerator.generate_mock_profiles(count=10)
```

### Development Notes

- Test data is regenerated on each request (not cached)
- All mock data uses deterministic IDs based on UUIDs
- Entity relationships are automatically generated
- Profile data matches realistic simulation parameters

### Next Steps

1. Start the development server: `npm run dev`
2. Test API endpoints using curl or Postman
3. Add your real API keys to `.env` when ready to use production APIs
4. Toggle TEST_MODE on/off based on your development needs

### Troubleshooting

**Frontend build fails?**
```bash
cd frontend
npm install
npm run dev
```

**Backend won't start?**
```bash
cd backend
python run.py
# Check the error message - most will show which keys are missing
```

**Test data not showing?**
- Verify `.env` has `TEST_MODE=true`
- Check Flask debug logs: `FLASK_DEBUG=true` in `.env`
- Ensure backend is running on port 5001

**Want to use real APIs?**
- Set `TEST_MODE=false` in `.env`
- Add real API keys: `LLM_API_KEY` and `ZEP_API_KEY`
- Restart the backend server
