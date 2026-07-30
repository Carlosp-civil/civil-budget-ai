from app.knowledge.manager import KnowledgeManager


manager = KnowledgeManager(
    "data/knowledge/column_aliases.json"
)

manager.load()

print(manager._knowledge_base)