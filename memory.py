import uuid

from datetime import datetime


from typing import Any


class MemoryNote:
    """메모리 시스템이 관리하는 단일 정보 단위를 표현"""

    def __init__(
        self,
        content: str,
        id: str | None = None,
        keywords: list[str] | None = None,
        links: list[dict[str, Any]] | None = None,
        retrieval_count: int | None = None,
        timestamp: str | None = None,
        last_accessed: str | None = None,
        context: str | None = None,
        evolution_history: list[Any] | None = None,
        category: str | None = None,
        tags: list[str] | None = None,
    ) -> None:
        """메모리 시스템을 초기화한다.

        Args:
            content (str): 메모리의 본문 텍스트.
            id (str | None, optional): 	UUID 기반 고유 식별자. None일 시, UUID가 자동으로 생성.
            keywords (list[str] | None, optional): 본문 텍스트로부터 LLM 또는 외부 분석기를 이용해 추출된 핵심 용어 목록.
            links (list[dict[str, Any]] | None, optional): 관련이 있는 메모리의 ID 리스트.
            retrieval_count (int | None, optional): 해당 메모리가 참조된 횟수.
            timestamp (str | None, optional): 생성 시각. YYYYMMDDHHMM 형식으로 표현.
            last_accessed (str | None, optional): 최근 참조 시각. YYYYMMDDHHMM 형식으로 표현.
            context (str | None, optional): 메모리 컨텐츠가 속한 상위 컨텍스트 또는 주제.
            evolution_history (list[Any] | None, optional): 메모리 변경 이력에 대한 정보.
            category (str | None, optional): 메모리 컨텐츠가 분류된 카테고리.
            tags (list[str] | None, optional): 추가 분류에 사용되는 카테고리 태그.
        """

        # 주요 컨텐츠 및 ID 설정
        self.content = content
        self.id = id or str(uuid.uuid4())

        # 시멘틱한 메타데이터 정보
        self.keywords = keywords or []
        self.links = links or []
        self.context = context or "General"
        self.category = category or "Uncategorized"
        self.tags = tags or []

        # 생성 및 접근 시각 정보
        current_time = datetime.now().strftime("%Y%m%d%H%M")
        self.timestamp = timestamp or current_time
        self.last_accessed = last_accessed or current_time

        # 조회 및 변경 이력 정보
        self.retrieval_count = retrieval_count or 0
        self.evolution_history = evolution_history or []
