"""
测试数据生成器 - 用于TEST_MODE模式提供虚拟数据而无需API密钥
"""

import uuid
from datetime import datetime
from typing import List, Dict, Any


class MockEntity:
    """模拟实体类"""
    def __init__(self, entity_id: str, name: str, entity_type: str, description: str):
        self.id = entity_id
        self.name = name
        self.type = entity_type
        self.description = description
        self.properties = {
            "age": 25 + (hash(entity_id) % 50),
            "location": ["New York", "London", "Tokyo", "Beijing"][hash(entity_id) % 4],
            "interests": ["Technology", "Music", "Sports", "Art", "Science"][(hash(entity_id) // 5) % 5:][:3]
        }
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "properties": self.properties
        }


class MockEntityCollection:
    """模拟实体集合"""
    def __init__(self, entities: List[MockEntity]):
        self.entities = entities
        self.filtered_count = len(entities)
        self.entity_types = set(e.type for e in entities)
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "filtered_count": self.filtered_count,
            "entity_types": list(self.entity_types),
            "entities": [e.to_dict() for e in self.entities],
            "edges": []
        }


class TestDataGenerator:
    """测试数据生成器"""
    
    # 预定义的实体类型
    ENTITY_TYPES = ["Student", "PublicFigure", "Organization", "Location", "Topic"]
    
    # 预定义的名称
    STUDENT_NAMES = [
        "Alice Johnson", "Bob Smith", "Carol Davis", "David Wilson", "Emma Brown",
        "Frank Miller", "Grace Lee", "Henry Taylor", "Iris Martin", "Jack Anderson"
    ]
    
    PUBLIC_FIGURE_NAMES = [
        "Elon Musk", "Oprah Winfrey", "Bill Gates", "Greta Thunberg", "Joe Rogan",
        "Taylor Swift", "The Rock", "Bezos", "Warren Buffett", "Satya Nadella"
    ]
    
    ORGANIZATION_NAMES = [
        "TechCorp Inc", "Global Solutions Ltd", "Innovation Hub", "Digital Dynamics",
        "Future Systems", "Cloud Pioneers", "AI Research Labs", "Data Analytics Co"
    ]
    
    @staticmethod
    def generate_entities(count: int = 10, entity_types: List[str] = None) -> List[MockEntity]:
        """生成虚拟实体列表"""
        if entity_types is None:
            entity_types = TestDataGenerator.ENTITY_TYPES
            
        entities = []
        for i in range(count):
            entity_type = entity_types[i % len(entity_types)]
            entity_id = f"entity_{uuid.uuid4().hex[:8]}"
            
            # 根据类型生成名称
            if entity_type == "Student":
                name = TestDataGenerator.STUDENT_NAMES[i % len(TestDataGenerator.STUDENT_NAMES)]
            elif entity_type == "PublicFigure":
                name = TestDataGenerator.PUBLIC_FIGURE_NAMES[i % len(TestDataGenerator.PUBLIC_FIGURE_NAMES)]
            elif entity_type == "Organization":
                name = TestDataGenerator.ORGANIZATION_NAMES[i % len(TestDataGenerator.ORGANIZATION_NAMES)]
            else:
                name = f"{entity_type}_{i}"
            
            description = f"Mock {entity_type} entity for testing purposes"
            entity = MockEntity(entity_id, name, entity_type, description)
            entities.append(entity)
            
        return entities
    
    @staticmethod
    def generate_mock_profiles(count: int = 5) -> Dict[str, Any]:
        """生成虚拟Reddit人设"""
        profiles = []
        for i in range(count):
            profile = {
                "entity_id": f"entity_{uuid.uuid4().hex[:8]}",
                "username": f"test_user_{i}",
                "reddit_name": f"reddit_user_{i}",
                "personality": f"Test personality profile #{i}",
                "behavior": f"Test behavior profile #{i}",
                "interests": ["technology", "science", "gaming"][i % 3:] + ["social"],
                "posting_frequency": "moderate",
                "engagement_level": ["high", "medium", "low"][i % 3]
            }
            profiles.append(profile)
        return profiles
    
    @staticmethod
    def generate_mock_twitter_profiles(count: int = 5) -> str:
        """生成虚拟Twitter人设 (CSV格式)"""
        headers = "entity_id,username,twitter_handle,profile_type,personality,behavior,engagement_level\n"
        rows = []
        for i in range(count):
            row = (
                f"entity_{uuid.uuid4().hex[:8]},"
                f"twitter_user_{i},"
                f"@test_handle_{i},"
                f"regular_user,"
                f"Test Twitter Personality #{i},"
                f"Active Twitter Behavior #{i},"
                f"{'high' if i % 2 == 0 else 'medium'}"
            )
            rows.append(row)
        return headers + "\n".join(rows)
    
    @staticmethod
    def generate_mock_simulation_config() -> Dict[str, Any]:
        """生成虚拟模拟配置"""
        return {
            "simulation_id": f"sim_{uuid.uuid4().hex[:8]}",
            "name": "Test Simulation",
            "description": "Mock simulation for testing",
            "max_rounds": 10,
            "agents_count": 5,
            "platforms": ["reddit", "twitter"],
            "created_at": datetime.now().isoformat(),
            "parameters": {
                "reddit_posts_per_round": 3,
                "twitter_tweets_per_round": 5,
                "interaction_probability": 0.7,
                "new_entity_probability": 0.1
            },
            "status": "ready"
        }
    
    @staticmethod
    def generate_mock_graph_entities(graph_id: str = None, count: int = 10) -> Dict[str, Any]:
        """生成虚拟图谱实体"""
        if not graph_id:
            graph_id = f"mirofish_{uuid.uuid4().hex[:8]}"
        
        entities = TestDataGenerator.generate_entities(count)
        
        return {
            "graph_id": graph_id,
            "filtered_count": len(entities),
            "entity_types": list(set(e.type for e in entities)),
            "entities": [e.to_dict() for e in entities],
            "edges": [
                {
                    "source": entities[i].id,
                    "target": entities[(i + 1) % len(entities)].id,
                    "relationship": ["knows", "works_with", "collaborates"][i % 3]
                }
                for i in range(len(entities) - 1)
            ]
        }
    
    @staticmethod
    def generate_mock_task_status() -> Dict[str, Any]:
        """生成虚拟任务状态"""
        return {
            "task_id": f"task_{uuid.uuid4().hex[:8]}",
            "status": "completed",
            "progress": 100,
            "message": "Test task completed successfully",
            "created_at": datetime.now().isoformat(),
            "completed_at": datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_mock_graph_data(graph_id: str = None) -> Dict[str, Any]:
        """生成虚拟图谱数据（用于图形可视化）- 包含600+节点用于测试"""
        if not graph_id:
            graph_id = f"mirofish_{uuid.uuid4().hex[:8]}"
        
        # 生成600个节点数据以测试大规模图形
        entity_count = 600
        entities = TestDataGenerator.generate_entities(count=entity_count)
        nodes = []
        for entity in entities:
            nodes.append({
                "id": entity.id,
                "label": entity.name,
                "type": entity.type,
                "size": 20 + (hash(entity.id) % 40),
                "color": {
                    "Student": "#FF5722",
                    "PublicFigure": "#2196F3",
                    "Organization": "#4CAF50",
                    "Location": "#FFC107",
                    "Topic": "#9C27B0"
                }.get(entity.type, "#999")
            })
        
        # 生成边数据 - 每个节点平均连接3个其他节点
        edges = []
        relationships = ["knows", "works_with", "collaborates", "follows", "mentions"]
        
        # 创建多层次的连接
        for i in range(len(entities)):
            # 连接相邻节点
            edges.append({
                "source": entities[i].id,
                "target": entities[(i + 1) % len(entities)].id,
                "relationship": relationships[i % len(relationships)]
            })
            # 连接间隔2个节点的节点
            if i < len(entities) - 2:
                edges.append({
                    "source": entities[i].id,
                    "target": entities[(i + 2) % len(entities)].id,
                    "relationship": relationships[(i + 1) % len(relationships)]
                })
            # 连接间隔5个节点的节点
            if i < len(entities) - 5:
                edges.append({
                    "source": entities[i].id,
                    "target": entities[(i + 5) % len(entities)].id,
                    "relationship": relationships[(i + 2) % len(relationships)]
                })
        
        return {
            "success": True,
            "graph_id": graph_id,
            "nodes": nodes,
            "node_count": len(nodes),
            "edges": edges,
            "edge_count": len(edges),
            "statistics": {
                "total_nodes": len(nodes),
                "total_edges": len(edges),
                "entity_types": list(set(e.type for e in entities)),
                "node_density": round(len(edges) / (len(nodes) * (len(nodes) - 1) / 2), 2) if len(nodes) > 1 else 0
            }
        }
