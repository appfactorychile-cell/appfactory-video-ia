from app.models.production import ProductionJob
from app.production import (
    asset_manager,
    effects_manager,
    learning_feedback,
    music_manager,
    quality_control,
    render_manager,
    scene_builder,
    script_generator,
    storyboard_generator,
    subtitle_manager,
    voice_manager,
)


def build_production_job(job: ProductionJob) -> ProductionJob:
    script = script_generator.generate_script(job.topic, job.country, job.language)
    job.hook = str(script["hook"])
    job.script = str(script["script"])
    job.storyboard = storyboard_generator.generate_storyboard(job.topic)
    job.scenes = scene_builder.build_scenes()
    job.assets = asset_manager.define_assets()
    job.narration = voice_manager.prepare_narration(job.script, job.language)
    job.subtitles = subtitle_manager.prepare_subtitles(job.language)
    job.music = music_manager.select_music(job.niche)
    job.effects = effects_manager.select_effects()
    job.render = render_manager.prepare_render()
    job.quality_report = quality_control.run_quality_control(job)
    job.learning_feedback = learning_feedback.build_learning_feedback(job.topic, job.hook)
    job.status = "Control de calidad listo"
    return job

