#!/usr/bin/env python3
"""Compatibility aliases for legacy English and new Chinese project metadata keys."""
from __future__ import annotations

ALIASES = {
    'schema_version': '\u7ed3\u6784\u7248\u672c',
    'skill_version': '\u6280\u80fd\u7248\u672c',
    'version': '\u7248\u672c',
    'status': '\u72b6\u6001',
    'project_profile_version': '\u4f5c\u54c1\u914d\u7f6e\u7248\u672c',
    'project_stage': '\u9879\u76ee\u9636\u6bb5',
    'last_consistent_chapter': '\u6700\u540e\u4e00\u81f4\u7ae0\u8282',
    'last_approved_chapter': '\u6700\u540e\u6279\u51c6\u7ae0\u8282',
    'writing_batch_size': '\u6b63\u6587\u6279\u6b21\u5927\u5c0f',
    'writing_batch_status': '\u6b63\u6587\u6279\u6b21\u72b6\u6001',
    'current_batch_id': '\u5f53\u524d\u6279\u6b21\u7f16\u53f7',
    'current_batch_start': '\u5f53\u524d\u6279\u6b21\u8d77\u59cb\u7ae0\u8282',
    'current_batch_end': '\u5f53\u524d\u6279\u6b21\u7ed3\u675f\u7ae0\u8282',
    'profile_status': '\u914d\u7f6e\u72b6\u6001',
    'profile_source': '\u914d\u7f6e\u6765\u6e90',
    'profile_confidence': '\u8bc6\u522b\u7f6e\u4fe1\u5ea6',
    'audience_profile': '\u53d7\u4f17\u7c7b\u578b',
    'age_range': '\u5e74\u9f84\u8303\u56f4',
    'audio_product_profile': '\u6709\u58f0\u4ea7\u54c1\u7c7b\u578b',
    'unit_length_mode': '\u5355\u5143\u5b57\u6570\u6a21\u5f0f',
    'unit_length_status': '\u5355\u5143\u5b57\u6570\u72b6\u6001',
    'unit_length_measure': '\u5355\u5143\u5b57\u6570\u8ba1\u91cf\u53e3\u5f84',
    'unit_length_source': '\u5355\u5143\u5b57\u6570\u6765\u6e90',
    'unit_target_chars': '\u5355\u5143\u76ee\u6807\u5b57\u6570',
    'unit_soft_min_chars': '\u5355\u5143\u8f6f\u4e0b\u9650',
    'unit_soft_max_chars': '\u5355\u5143\u8f6f\u4e0a\u9650',
    'unit_hard_max_chars': '\u5355\u5143\u786c\u4e0a\u9650',
    'script_format_profile': '\u8bdd\u672c\u683c\u5f0f\u914d\u7f6e',
    'docx_layout_profile': 'DOCX\u7248\u5f0f\u914d\u7f6e',
    'chapter_outline_delivery_format': '\u7ae0\u7eb2\u4ea4\u4ed8\u683c\u5f0f',
    'manuscript_delivery_format': '\u6b63\u6587\u4ea4\u4ed8\u683c\u5f0f',
    'narration_ratio_target': '\u65c1\u767d\u6bd4\u4f8b\u76ee\u6807',
    'narration_ratio_max': '\u65c1\u767d\u6bd4\u4f8b\u4e0a\u9650',
    'narration_paragraph_max': '\u5355\u6bb5\u65c1\u767d\u4e0a\u9650',
    'early_hook_chars': '\u524d\u6bb5\u94a9\u5b50\u5b57\u6570',
    'highlight_interval_chars': '\u770b\u70b9\u95f4\u9694\u5b57\u6570',
    'length_mode': '\u4f53\u91cf\u6a21\u5f0f',
    'output_mode': '\u8f93\u51fa\u6a21\u5f0f',
    'chapter_id': '\u7ae0\u8282\u7f16\u53f7',
    'chapter_number': '\u7ae0\u8282\u5e8f\u53f7',
    'volume': '\u5377\u53f7',
    'pov': '\u89c6\u89d2\u4eba\u7269',
    'chapter_type': '\u7ae0\u8282\u7c7b\u578b',
    'content_status': '\u6b63\u6587\u72b6\u6001',
    'content_revision': '\u6b63\u6587\u4fee\u8ba2\u7248\u672c',
    'batch_id': '\u6279\u6b21\u7f16\u53f7',
    'approved_project_profile_version': '\u5df2\u6279\u51c6\u4f5c\u54c1\u914d\u7f6e\u7248\u672c',
    'approved_outline_version': '\u5df2\u6279\u51c6\u5168\u4e66\u5927\u7eb2\u7248\u672c',
    'source_chapter_outline_version': '\u6765\u6e90\u7ae0\u7eb2\u7248\u672c',
    'validity': '\u5185\u5bb9\u6709\u6548\u6027',
}

VALUE_ALIASES = {
    'project_stage': {
        '\u4f5c\u54c1\u914d\u7f6e\u786e\u8ba4': 'PROFILE_RESOLUTION',
        '\u4f5c\u54c1\u914d\u7f6e\u7528\u6237\u5ba1\u6838': 'PROFILE_USER_REVIEW',
        '\u4e16\u754c\u89c2\u6574\u7406': 'WORLDVIEW_INTAKE',
        '\u5168\u4e66\u5927\u7eb2\u8349\u62df': 'BOOK_OUTLINE_DRAFTING',
        '\u5168\u4e66\u5927\u7eb2\u5185\u90e8\u5ba1\u6838': 'BOOK_OUTLINE_INTERNAL_REVIEW',
        '\u5168\u4e66\u5927\u7eb2\u7528\u6237\u5ba1\u6838': 'BOOK_OUTLINE_USER_REVIEW',
        '\u4f53\u91cf\u9501\u5b9a': 'LENGTH_LOCK',
        '\u7ae0\u7eb2\u8349\u62df': 'CHAPTER_OUTLINE_DRAFTING',
        '\u7ae0\u7eb2\u5185\u90e8\u5ba1\u6838': 'CHAPTER_OUTLINE_INTERNAL_REVIEW',
        '\u7ae0\u7eb2\u7528\u6237\u5ba1\u6838': 'CHAPTER_OUTLINE_USER_REVIEW',
        '\u6b63\u6587\u5199\u4f5c': 'WRITING',
        '\u5df2\u5b8c\u6210': 'COMPLETED',
    },
    'profile_status': {
        '\u5f85\u786e\u8ba4': 'pending', '\u7b49\u5f85\u7528\u6237\u786e\u8ba4': 'awaiting_user_approval', '\u5df2\u6279\u51c6': 'approved',
    },
    'audience_profile': {
        '\u672a\u8bc6\u522b': 'unknown', '\u6210\u4eba': 'adult', '8-12\u5c81\u5c11\u513f': 'children_8_12', '\u81ea\u5b9a\u4e49': 'custom',
    },
    'audio_product_profile': {
        '\u672a\u8bc6\u522b': 'unknown', '\u6210\u4eba\u957f\u7bc7\u7f51\u6587\u6709\u58f0\u4e66': 'adult_longform_webnovel',
        '\u5c11\u513f\u5206\u96c6\u6545\u4e8b': 'children_episodic_story', '\u5c11\u513f\u957f\u7ae0\u6545\u4e8b': 'children_chaptered_story',
        '\u513f\u7ae5\u7ed8\u672c\u6709\u58f0\u5316': 'children_picturebook_audio',
    },
    'unit_length_mode': {
        '\u672a\u8bbe\u7f6e': 'unset', '\u7cbe\u786e\u5b57\u6570': 'user_exact', '\u5b57\u6570\u8303\u56f4': 'user_range',
        '\u53c2\u8003\u6837\u7a3f': 'reference_sample', 'Skill\u5efa\u8bae': 'skill_recommended', '\u7075\u6d3b': 'flexible',
    },
    'unit_length_status': {
        '\u5f85\u786e\u8ba4': 'pending', '\u5df2\u6279\u51c6': 'approved', '\u5df2\u9501\u5b9a': 'locked',
    },
    'unit_length_measure': {
        '\u6709\u6548\u6b63\u6587\u5b57\u7b26\u6570': 'effective_content_chars', '\u6210\u54c1\u53ef\u89c1\u5b57\u7b26\u6570': 'finished_visible_chars', '\u81ea\u5b9a\u4e49': 'custom',
    },
    'writing_batch_status': {
        '\u9501\u5b9a': 'locked', '\u5c31\u7eea': 'ready', '\u8349\u62df\u4e2d': 'drafting', '\u7b49\u5f85\u7528\u6237\u786e\u8ba4': 'awaiting_user_approval',
        '\u4fee\u8ba2\u4e2d': 'revising', '\u5df2\u6279\u51c6': 'approved',
    },
    'content_status': {
        '\u8349\u7a3f': 'draft', '\u7b49\u5f85\u7528\u6237\u786e\u8ba4': 'awaiting_user_approval', '\u5df2\u6279\u51c6': 'approved',
        '\u5df2\u5931\u6548': 'stale', '\u5df2\u66ff\u4ee3': 'superseded',
    },
    'validity': {
        '\u5f53\u524d\u6709\u6548': 'current', '\u5f85\u590d\u6838': 'revalidate', '\u5df2\u5931\u6548': 'stale', '\u5df2\u66ff\u4ee3': 'superseded',
    },
    'status': {
        '\u672a\u5f00\u59cb': 'not_started', '\u8349\u62df\u4e2d': 'drafting', '\u8349\u7a3f': 'draft', '\u5185\u90e8\u5ba1\u6838': 'internal_review',
        '\u7b49\u5f85\u7528\u6237\u786e\u8ba4': 'awaiting_user_approval', '\u5df2\u6279\u51c6': 'approved', '\u9501\u5b9a': 'locked',
        '\u4fee\u8ba2\u4e2d': 'revising', '\u7075\u6d3b': 'flexible',
    },
}


def getv(meta: dict[str, str], key: str, default=None):
    if key in meta:
        raw = meta[key]
    else:
        zh = ALIASES.get(key)
        if zh is not None and zh in meta:
            raw = meta[zh]
        else:
            return default
    return VALUE_ALIASES.get(key, {}).get(raw, raw)
