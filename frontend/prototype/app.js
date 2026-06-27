const screens = [
  { id: "login", label: "Login", icon: "IN", kpi: "Access" },
  { id: "dashboard", label: "Global Command Center", icon: "GC", kpi: "Live" },
  { id: "mvp-workflow", label: "MVP Workflow", icon: "WF", kpi: "Flow" },
  { id: "intelligence", label: "Centro de Inteligencia Global", icon: "IG", kpi: "392" },
  { id: "global-intelligence", label: "Global Intelligence Engine", icon: "GIE", kpi: "Brain" },
  { id: "digital-factory", label: "Digital Content Factory", icon: "DF", kpi: "24/7" },
  { id: "global-factory", label: "Global Factory", icon: "GF", kpi: "Live" },
  { id: "end-to-end-pipeline", label: "End to End Pipeline", icon: "EE", kpi: "16" },
  { id: "video-factory-live", label: "Video Factory Live", icon: "VL", kpi: "Queue" },
  { id: "ai-workers", label: "AI Workers", icon: "AW", kpi: "11" },
  { id: "multi-channel-manager", label: "Multi Channel Manager", icon: "MC", kpi: "80" },
  { id: "world-scheduler", label: "World Scheduler", icon: "WS", kpi: "TZ" },
  { id: "factory-monetization", label: "Factory Monetization", icon: "FM", kpi: "$" },
  { id: "mission-control", label: "Mission Control", icon: "MS", kpi: "CEO" },
  { id: "full-video-journey", label: "Full Video Journey", icon: "FJ", kpi: "001" },
  { id: "executive-overview", label: "Executive Overview", icon: "XO", kpi: "Board" },
  { id: "learning-engine", label: "Learning & Evolution Engine", icon: "LE", kpi: "Evolve" },
  { id: "memory-engine", label: "Memory Engine", icon: "ME", kpi: "Core" },
  { id: "channel-memory", label: "Channel Memory", icon: "CM", kpi: "DNA" },
  { id: "country-memory", label: "Country Memory", icon: "CY", kpi: "World" },
  { id: "language-memory", label: "Language Memory", icon: "LM", kpi: "9" },
  { id: "experiment-engine", label: "Experiment Engine", icon: "EX", kpi: "A/B/C" },
  { id: "creative-evolution", label: "Creative Evolution", icon: "CE", kpi: "AI" },
  { id: "global-knowledge", label: "Global Knowledge", icon: "GK", kpi: "Vault" },
  { id: "ai-self-improvement", label: "AI Self Improvement", icon: "SI", kpi: "Today" },
  { id: "global-learning-map", label: "Global Learning Map", icon: "GL", kpi: "Map" },
  { id: "next-best-action", label: "Next Best Action", icon: "NB", kpi: "Now" },
  { id: "story-director", label: "Story Director AI", icon: "SD", kpi: "Creative" },
  { id: "video-style-lab", label: "Video Style Lab", icon: "VS", kpi: "14" },
  { id: "character-scene", label: "Character & Scene Builder", icon: "CS", kpi: "Scene" },
  { id: "hook-retention", label: "Hook vs Retention Simulator", icon: "HR", kpi: "A/B" },
  { id: "vertical-blueprint", label: "Vertical Video Blueprint", icon: "VB", kpi: "9:16" },
  { id: "smart-duration", label: "Smart Duration Engine", icon: "DU", kpi: "20-45" },
  { id: "attention-engine", label: "Attention Engine", icon: "AE", kpi: "91" },
  { id: "retention-engine", label: "Retention Engine", icon: "RE", kpi: "88" },
  { id: "opportunity-radar", label: "Global Opportunity Radar", icon: "OR", kpi: "Radar" },
  { id: "competitor-intelligence", label: "Competitor Intelligence", icon: "CI", kpi: "Ethic" },
  { id: "content-pipeline", label: "Content Pipeline", icon: "CP", kpi: "12" },
  { id: "editorial-director", label: "Editorial Director AI", icon: "ED", kpi: "Why" },
  { id: "content-heatmap", label: "Global Content Heatmap", icon: "GH", kpi: "Hot" },
  { id: "decision-timeline", label: "AI Decision Timeline", icon: "DT", kpi: "08:18" },
  { id: "quality-dashboard", label: "Quality Dashboard", icon: "QD", kpi: "94" },
  { id: "viral-psychology", label: "Viral Psychology Engine", icon: "VP", kpi: "92" },
  { id: "channel-dna", label: "Channel DNA", icon: "DNA", kpi: "248" },
  { id: "quality-gate", label: "Content Quality Gate", icon: "QG", kpi: "Safe" },
  { id: "entertainment-scoring", label: "Entertainment Scoring", icon: "ES", kpi: "88" },
  { id: "idea-lab", label: "Idea Lab", icon: "IL", kpi: "36" },
  { id: "hook-builder", label: "Hook Builder", icon: "HB", kpi: "5x" },
  { id: "curiosity-map", label: "Audience Curiosity Map", icon: "AC", kpi: "Map" },
  { id: "trends", label: "Mapa mundial de tendencias", icon: "MT", kpi: "Hot" },
  { id: "trend-country", label: "Tendencias por pais", icon: "TP", kpi: "38" },
  { id: "trend-language", label: "Tendencias por idioma", icon: "TI", kpi: "6" },
  { id: "channels", label: "Rendimiento por canal", icon: "RC", kpi: "248" },
  { id: "countries", label: "Rendimiento por pais", icon: "RP", kpi: "38" },
  { id: "languages", label: "Rendimiento por idioma", icon: "RI", kpi: "6" },
  { id: "calendar", label: "Calendario mundial", icon: "CM", kpi: "24h" },
  { id: "videos", label: "Cola mundial de videos", icon: "CV", kpi: "1.9K" },
  { id: "queue", label: "Estado de renderizado", icon: "ER", kpi: "684" },
  { id: "publish", label: "Estado de publicacion", icon: "EP", kpi: "API" },
  { id: "ai-engine", label: "Estado de cada IA", icon: "AI", kpi: "9" },
  { id: "agents", label: "Centro de agentes IA", icon: "AG", kpi: "27" },
  { id: "automation", label: "Centro de automatizacion", icon: "CA", kpi: "4x" },
  { id: "apis", label: "Estado de APIs", icon: "AP", kpi: "4" },
  { id: "monetization", label: "Centro de monetizacion", icon: "MO", kpi: "$" },
  { id: "costs", label: "Costos operacionales", icon: "CO", kpi: "Ops" },
  { id: "system", label: "Estado de servidores", icon: "ES", kpi: "99.97" },
  { id: "settings", label: "Configuracion", icon: "CF", kpi: "Admin" },
  { id: "company", label: "Perfil de Empresa", icon: "PE", kpi: "AFC" }
];

const metrics = [
  ["Canales activos", "248", "+18 este mes", "ok"],
  ["Videos publicados hoy", "1.984", "68% del plan", "ok"],
  ["Videos en proceso", "684", "112 renderizando", "warn"],
  ["Visualizaciones 24h", "48.6M", "+22.4%", "ok"],
  ["Ingresos estimados", "$286K", "+11.8%", "ok"],
  ["Costo operativo", "$18.7K", "6.5% revenue", "warn"]
];

const statuses = [
  ["Estado de servidores", "Multi-region operativo", "OK", "ok"],
  ["Estado IA", "9 agentes simulados disponibles", "OK", "ok"],
  ["Estado renderizado", "Alta demanda en Europa", "Atencion", "warn"],
  ["Estado publicacion", "Colas saludables", "OK", "ok"],
  ["Estado APIs", "YouTube/Meta/TikTok pendientes de integracion real", "Mock", "warn"],
  ["Centro de automatizacion", "4 bloques diarios activos por canal", "Live", "info"]
];

const countryRows = [
  ["Estados Unidos", "Ingles", "Tecnologia / finanzas", "412", "12.8M", "$84.2K", "En expansion"],
  ["Mexico", "Espanol", "IA practica", "286", "7.4M", "$39.6K", "Alta traccion"],
  ["Brasil", "Portugues", "Energia / negocios", "244", "5.9M", "$28.1K", "Creciente"],
  ["Francia", "Frances", "Viajes / estilo", "198", "3.6M", "$17.4K", "Estable"],
  ["Alemania", "Aleman", "Educacion / productividad", "176", "3.1M", "$15.9K", "Competitivo"],
  ["Italia", "Italiano", "Turismo / cultura", "152", "2.4M", "$11.8K", "Creciente"]
];

const languageRows = [
  ["Espanol", "92 canales", "684 videos", "16.8M views", "$72.4K", "Localizacion LATAM"],
  ["Ingles", "74 canales", "596 videos", "19.2M views", "$104.8K", "Global premium"],
  ["Portugues", "31 canales", "248 videos", "5.9M views", "$28.1K", "Brasil foco"],
  ["Frances", "21 canales", "168 videos", "3.6M views", "$17.4K", "Europa"],
  ["Italiano", "16 canales", "128 videos", "2.4M views", "$11.8K", "Turismo"],
  ["Aleman", "14 canales", "112 videos", "3.1M views", "$15.9K", "B2B" ]
];

const channelRows = [
  ["AI Finance Daily", "US", "Ingles", "Finanzas", "184", "8.4M", "$42.8K", "Activo"],
  ["Futuro Latino IA", "MX", "Espanol", "Tecnologia", "168", "6.9M", "$31.2K", "Activo"],
  ["Brasil Solar News", "BR", "Portugues", "Energia", "116", "3.1M", "$14.7K", "Revision"],
  ["Europe Travel Pulse", "FR", "Frances", "Viajes", "104", "2.8M", "$12.9K", "Activo"],
  ["Deutschland AI Lernen", "DE", "Aleman", "Educacion", "96", "2.1M", "$10.4K", "Activo"]
];

const trendRows = [
  ["AI agents for finance", "Estados Unidos", "Ingles", "96", "Hot"],
  ["Herramientas IA para negocios", "Mexico", "Espanol", "94", "Hot"],
  ["Energia solar residencial", "Brasil", "Portugues", "88", "Creciente"],
  ["Travel automation", "Francia", "Frances", "83", "Estable"],
  ["Produktivitat mit KI", "Alemania", "Aleman", "81", "Competitivo"],
  ["Turismo inteligente", "Italia", "Italiano", "78", "Creciente"]
];

const aiRows = [
  ["TrendMind Global", "Analisis de tendencias", "99.2%", "Activo"],
  ["ResearchCore", "Investigacion y contexto", "98.7%", "Activo"],
  ["ScriptForge", "Guiones originales", "97.9%", "Activo"],
  ["LocalizeX", "Adaptacion cultural", "98.1%", "Activo"],
  ["VoiceGrid", "Narracion multidioma", "96.4%", "Alta carga"],
  ["SubtitleSync", "Subtitulos sincronizados", "99.0%", "Activo"],
  ["RenderPilot", "Edicion y composicion", "94.8%", "Alta carga"],
  ["PublishGate", "Publicacion oficial", "Mock", "Pendiente"],
  ["MetricSense", "Analitica y recomendaciones", "98.5%", "Activo"]
];

const queueRows = [
  ["North America cluster", "Trend scan", "AI Finance Daily", 96, "Finalizando"],
  ["LATAM cluster", "Script generation", "Futuro Latino IA", 72, "Procesando"],
  ["Brazil cluster", "Voiceover", "Brasil Solar News", 44, "En cola"],
  ["Europe cluster", "Subtitles", "Europe Travel Pulse", 58, "Procesando"],
  ["Render farm EU-2", "9:16 render", "Deutschland AI Lernen", 31, "Renderizando"],
  ["Global publishing", "API dispatch", "Travel Pulse", 84, "Validando" ]
];

const costRows = [
  ["IA texto", "$4.820", "25.7%", "Controlado"],
  ["IA voz", "$3.940", "21.1%", "Normal"],
  ["Renderizado", "$5.210", "27.8%", "Alta demanda"],
  ["Storage", "$1.880", "10.0%", "Controlado"],
  ["APIs / integraciones", "$740", "3.9%", "Mock"],
  ["Infraestructura", "$2.110", "11.5%", "Normal"]
];

const viralFactors = [
  ["Curiosidad", 94, "Pregunta abierta que invita a seguir mirando"],
  ["Sorpresa", 87, "Giro inesperado sin exagerar ni inventar"],
  ["Emocion", 82, "Conecta con aspiracion, miedo sano o alivio"],
  ["Humor", 68, "Ligero, respetuoso y localizable"],
  ["Utilidad", 96, "El espectador se lleva una idea aplicable"],
  ["Potencial de comentarios", 89, "Provoca opinion sin crear conflicto falso"],
  ["Potencial de compartir", 91, "Dato facil de reenviar a otra persona"],
  ["Retencion esperada", 88, "Hook fuerte, desarrollo rapido, cierre claro"]
];

const channelDnaRows = [
  ["AI Finance Daily", "Preciso y ambicioso", "Directo premium", "Profesionales 25-44", "Medio-alto", "Cinematico sobrio", "Narrador experto", "45s", "Nadie te cuenta esto...", "Rumores bursatiles", "IA aplicada a dinero"],
  ["Futuro Latino IA", "Curioso y cercano", "Conversacional", "Emprendedores LATAM", "Medio", "Energia visual alta", "Narradora calida", "38s", "Esto esta pasando...", "Promesas falsas", "Herramientas utiles"],
  ["Brasil Solar News", "Optimista y practico", "Claro", "Familias y pymes", "Basico-medio", "Solar limpio", "Narrador confiable", "42s", "Este dato parece mentira...", "Datos no verificados", "Ahorro y energia"],
  ["Europe Travel Pulse", "Elegante y aspiracional", "Editorial", "Viajeros premium", "Ligero", "Documental moderno", "Narradora serena", "35s", "Lo que ocurrio despues...", "Clickbait ofensivo", "Lugares y cultura"]
];

const qualityChecks = [
  ["El inicio engancha en 3 segundos", "Aprobado", "Hook claro antes del segundo 2.4"],
  ["El guion es original", "Aprobado", "No replica videos virales ni estructuras copiadas"],
  ["Tiene valor real", "Aprobado", "Entrega contexto, utilidad o una idea memorable"],
  ["Evita rumores falsos", "Aprobado", "Bloquea afirmaciones no verificadas"],
  ["Respeta derechos de autor", "Aprobado", "No usa clips, musica o guiones protegidos"],
  ["Esta localizado al pais e idioma", "Revision", "Ajustar expresiones locales antes de producir"],
  ["Tiene potencial de conversacion", "Aprobado", "Cierra con una pregunta responsable"]
];

const entertainmentScores = [
  ["Interesante", 93, "La premisa abre una brecha de curiosidad"],
  ["Copuchento/curioso", 84, "Tiene misterio sin caer en rumor"],
  ["Compartible", 89, "Se entiende rapido y sirve para conversar"],
  ["Comentable", 91, "Invita opinion con una pregunta segura"],
  ["Facil de entender", 95, "Una idea por video, lenguaje simple"],
  ["Visualmente atractivo", 86, "Escenas comparativas y datos en pantalla"],
  ["Monetizable", 78, "Nicho con demanda comercial"],
  ["Riesgo de baja calidad", 18, "Bajo, requiere mantener fuentes verificadas"]
];

const ideaLabRows = [
  ["Idea original", "La nueva forma en que pequenos negocios usan IA para ahorrar tiempo"],
  ["Version mas entretenida", "Un negocio comun hizo esto con IA y recupero 10 horas a la semana"],
  ["Version mas emocional", "La herramienta que le devolvio tiempo libre a una emprendedora"],
  ["Version mas polemica pero segura", "La IA no reemplazo al equipo: elimino la tarea que nadie queria hacer"],
  ["Version educativa", "Tres automatizaciones simples que cualquier pyme puede entender"],
  ["Version corta Shorts/Reels/TikTok", "La tarea que una IA puede resolver antes de tu segundo cafe"]
];

const hookRows = [
  ["Nadie te cuenta esto...", 92, "Misterio directo", "Usar solo si el video entrega una revelacion real"],
  ["Esto esta pasando y pocos lo notaron...", 89, "Tendencia emergente", "Ideal para datos recientes verificados"],
  ["La razon por la que todos hablan de esto...", 84, "Contexto social", "Evitar si no hay volumen real de conversacion"],
  ["Este dato parece mentira, pero...", 90, "Sorpresa factual", "Debe estar respaldado por fuente permitida"],
  ["Lo que ocurrio despues sorprendio a todos...", 81, "Narrativa", "No usar para exagerar eventos sensibles"]
];

const curiosityRows = [
  ["Mexico", "Espanol", "Tecnologia practica", "Herramientas IA para ganar tiempo", "Curiosidad + utilidad", "Muy alto"],
  ["Estados Unidos", "Ingles", "Finanzas", "Automatizacion de ingresos y productividad", "Utilidad + ambicion", "Alto"],
  ["Brasil", "Portugues", "Energia", "Ahorro familiar y negocios solares", "Utilidad + sorpresa", "Alto"],
  ["Francia", "Frances", "Viajes", "Destinos inteligentes y cultura", "Emocion + belleza", "Medio-alto"],
  ["Alemania", "Aleman", "Educacion", "Productividad verificable con IA", "Claridad + evidencia", "Medio-alto"],
  ["Italia", "Italiano", "Turismo", "Historias breves de lugares y comida", "Emocion + curiosidad", "Alto"]
];

const guardrailRows = [
  "No crear contenido falso",
  "No difundir rumores no verificados",
  "No copiar videos virales",
  "No generar contenido ofensivo",
  "No buscar vistas falsas",
  "No manipular algoritmos",
  "Crear contenido original, entretenido y responsable"
];

const opportunityRows = [
  ["Mexico", "IA para pymes", "Espanol", "Baja", "Alta", "13:00 / 21:00", 94],
  ["Brasil", "Energia y ahorro", "Portugues", "Media", "Alta", "08:00 / 17:00", 88],
  ["Estados Unidos", "AI agents", "Ingles", "Alta", "Muy alta", "08:00 / 13:00", 86],
  ["Italia", "Turismo inteligente", "Italiano", "Baja", "Media-alta", "17:00 / 21:00", 82],
  ["Alemania", "Productividad B2B", "Aleman", "Media", "Alta", "08:00 / 17:00", 80]
];

const competitorInsights = [
  ["Formato exitoso", "Explicador rapido con dato visual", "Crear estructura propia, no copiar videos"],
  ["Duracion recomendada", "34s - 48s", "Depende del pais, idioma y complejidad"],
  ["Frecuencia", "4 bloques diarios por canal", "Mantener calidad antes que volumen"],
  ["Tendencia general", "IA practica para ahorrar tiempo", "Validar fuentes y evitar promesas falsas"],
  ["Nivel de competencia", "Medio-alto", "Buscar angulos originales y locales"]
];

const pipelineStages = [
  ["Idea", "Listo", "00:35", "TrendMind Global"],
  ["Investigacion", "En curso", "02:10", "ResearchCore"],
  ["Guion", "Pendiente", "01:40", "ScriptForge"],
  ["Revision Editorial", "Pendiente", "00:55", "Editorial Director AI"],
  ["Narracion IA", "Pendiente", "01:20", "VoiceGrid"],
  ["Storyboard", "Pendiente", "01:15", "RenderPilot"],
  ["Video", "Pendiente", "03:50", "RenderPilot"],
  ["Subtitulos", "Pendiente", "00:50", "SubtitleSync"],
  ["Control de Calidad", "Pendiente", "01:05", "Quality Gate"],
  ["Programacion", "Pendiente", "00:25", "Scheduler AI"],
  ["Publicado", "Pendiente", "API mock", "PublishGate"],
  ["Analitica", "Pendiente", "24h", "MetricSense"]
];

const editorialRecommendation = [
  ["Tema", "Como pequenas empresas usan IA para recuperar tiempo operativo"],
  ["Curiosidad", "Alta: conecta con una pregunta diaria de negocios reales"],
  ["Valor educativo", "Alto: explica tres usos concretos sin vender humo"],
  ["Potencial de comentarios", "Alto: invita a contar que tarea automatizarian"],
  ["Potencial de compartir", "Alto: util para duenos de pymes y equipos pequenos"],
  ["Nivel de competencia", "Medio: muchos hablan de IA, pocos localizan ejemplos"],
  ["Publico objetivo", "Emprendedores, operadores y creadores de 25 a 44"],
  ["Nivel de monetizacion", "Alto: herramientas SaaS, productividad y educacion"],
  ["Riesgo", "Bajo si se evitan promesas financieras y datos no verificados"],
  ["Recomendacion final", "Producir version educativa + hook de curiosidad responsable"]
];

const decisionTimeline = [
  ["08:00", "Se detecto tendencia", "Mexico y Colombia suben busquedas sobre IA para pymes"],
  ["08:02", "Se aprobo investigacion", "ResearchCore valida fuentes permitidas y contexto local"],
  ["08:05", "Se genero guion", "ScriptForge produce una version original de 42 segundos"],
  ["08:09", "Narracion", "VoiceGrid prepara voz calida en espanol LATAM"],
  ["08:12", "Revision editorial", "Quality Gate marca localizacion como necesaria"],
  ["08:15", "Video listo", "RenderPilot entrega version 9:16 con subtitulos"],
  ["08:18", "Programado", "Scheduler AI recomienda publicacion a las 13:00"]
];

const qualityDashboardScores = [
  ["Originalidad", 96, "No replica formatos virales ni guiones existentes"],
  ["Valor para el usuario", 94, "Entrega accion practica y contexto"],
  ["Claridad", 91, "Una idea principal, lenguaje simple"],
  ["Retencion estimada", 88, "Hook rapido y ritmo sostenido"],
  ["Enganche inicial", 93, "Promesa clara en los primeros 3 segundos"],
  ["Potencial viral", 86, "Compartible sin exageracion"],
  ["Seguridad", 97, "Sin rumores, ataques ni afirmaciones sensibles"],
  ["Cumplimiento de politicas", 98, "Respeta derechos y APIs oficiales"]
];

const storyDirectorRows = [
  ["Idea seleccionada", "Como una pyme recupera 10 horas semanales usando IA simple"],
  ["Publico objetivo", "Emprendedores, operadores y creadores de 25 a 44"],
  ["Pais", "Mexico"],
  ["Idioma", "Espanol LATAM"],
  ["Emocion principal", "Alivio y curiosidad"],
  ["Objetivo del video", "Mostrar utilidad real sin prometer resultados falsos"],
  ["Estilo recomendado", "Hiperrealista documental corto"],
  ["Personaje recomendado", "Fundadora de pyme, cercana y creible"],
  ["Escenario recomendado", "Oficina pequena con movimiento cotidiano"],
  ["Ritmo recomendado", "Rapido al inicio, pausas breves en datos clave"],
  ["Duracion recomendada", "38 segundos"],
  ["Recomendacion final", "Producir version educativa con misterio moderado y cierre conversable"]
];

const storyLevels = [
  ["Nivel de misterio", 82, "Abre una pregunta sin crear rumor"],
  ["Nivel de humor", 54, "Ligero y humano, no protagonista"],
  ["Nivel de emocion", 78, "Alivio por recuperar tiempo"],
  ["Nivel educativo", 91, "Tres aprendizajes claros"],
  ["Nivel cinematografico", 84, "Luz premium y escenas realistas"]
];

const styleLabRows = [
  ["Hiperrealista", 92, 88, "Alto", "Medio", "Alta"],
  ["Cinematico", 89, 86, "Alto", "Medio", "Alta"],
  ["Documental", 84, 90, "Medio", "Medio", "Media"],
  ["Animacion 3D", 81, 78, "Alto", "Alto", "Alta"],
  ["Personaje IA", 86, 82, "Medio", "Medio", "Media"],
  ["Misterio", 91, 85, "Medio", "Bajo", "Media"],
  ["Horror suave", 76, 72, "Medio", "Medio", "Media"],
  ["Humor", 88, 80, "Bajo", "Bajo", "Media"],
  ["Educativo", 83, 87, "Bajo", "Bajo", "Baja"],
  ["Storytelling emocional", 90, 91, "Medio", "Medio", "Media"],
  ["Noticias rapidas", 79, 74, "Bajo", "Bajo", "Baja"],
  ["Minimalista", 72, 76, "Bajo", "Bajo", "Baja"],
  ["Retro", 70, 71, "Bajo", "Medio", "Media"],
  ["Futurista", 87, 82, "Medio", "Medio", "Alta"]
];

const characterSceneRows = [
  ["Tipo de personaje", "Emprendedora realista", "Humana, creible, no celebridad"],
  ["Edad aproximada", "32-42", "Adulto profesional joven"],
  ["Vestimenta", "Casual premium", "Camisa clara, accesorios simples"],
  ["Expresion", "Concentrada y luego aliviada", "Micro narrativa emocional"],
  ["Color predominante", "Azul profundo + verde energia", "Identidad APP FACTORY"],
  ["Tipo de camara", "Camara movil estabilizada", "Sensacion documental"],
  ["Plano", "Medio corto + inserts", "Rostro, manos, pantalla"],
  ["Movimiento", "Push-in suave", "Aumenta tension al dato fuerte"],
  ["Iluminacion", "Contraste suave premium", "No oscuro, no dramatico falso"],
  ["Ambiente", "Oficina pequena tecnologica", "Cercano y aspiracional"],
  ["Escenario", "Mesa de trabajo + laptop", "Contexto productivo"],
  ["Nivel de realismo", "92/100", "Hiperrealista controlado"],
  ["Estilo artistico", "Documental SaaS premium", "Elegante, util, mundial"]
];

const hookRetentionRows = [
  ["Hook A", "Nadie te cuenta esto sobre automatizar tu negocio...", 91, 84, 76, 68, 73, 66, 72],
  ["Hook B", "Esto esta pasando y pocos emprendedores lo notaron...", 94, 88, 81, 74, 78, 71, 79],
  ["Hook C", "La razon por la que algunos negocios recuperan horas cada semana...", 87, 82, 78, 72, 70, 64, 76],
  ["Hook D", "Este dato parece mentira, pero una IA puede resolverlo antes del cafe...", 96, 86, 75, 63, 82, 74, 70]
];

const blueprintRows = [
  ["Hook", "0-3s", "Pregunta curiosa", "Subtitulo grande", "Pulse suave", "Zoom rapido"],
  ["Escena 1", "3-7s", "Problema cotidiano", "Texto corto", "Beat bajo", "Plano medio"],
  ["Escena 2", "7-12s", "IA entra como ayuda", "Palabra clave", "Click sutil", "Insert pantalla"],
  ["Cambio de ritmo", "12-16s", "Corte dinamico", "Cambio tipografico", "Riser", "Whip pan"],
  ["Dato fuerte", "16-24s", "10 horas recuperadas", "Numero protagonista", "Hit suave", "Push-in"],
  ["Giro", "24-31s", "No reemplazo personas", "Contraste", "Silencio breve", "Close-up"],
  ["Conclusion", "31-36s", "Automatizar tareas repetidas", "Resumen", "Melodia clara", "Plano abierto"],
  ["CTA suave", "36-40s", "Que tarea automatizarias?", "Pregunta final", "Outro corto", "Zoom out"],
  ["Fin", "40-42s", "Logo discreto", "Sin saturar", "Cierre", "Fade"]
];

const durationRows = [
  ["Hook ultra rapido", "10-15s", "Impacto instantaneo", "Shorts/Reels/TikTok"],
  ["Dato curioso", "20-35s", "Explicar una sorpresa", "Shorts/Reels/TikTok"],
  ["Historia corta", "35-60s", "Mini arco emocional", "Shorts/Reels/TikTok"],
  ["Explicacion breve", "60-90s", "Mayor claridad", "Shorts/YouTube"],
  ["Mini documental", "90-180s", "Contexto y profundidad", "YouTube"],
  ["YouTube largo", "5-15 min", "Analisis extendido", "YouTube" ]
];

const durationDecisionRows = [
  ["Tipo de contenido", "Historia corta util"],
  ["Pais", "Mexico"],
  ["Idioma", "Espanol LATAM"],
  ["Nicho", "IA practica para pymes"],
  ["Complejidad", "Media"],
  ["Retencion esperada", "88/100"],
  ["Plataforma", "TikTok, Instagram Reels, YouTube Shorts"],
  ["Competencia", "Media-alta"],
  ["Objetivo", "Educar y provocar comentarios"],
  ["Decision automatica", "38 segundos"],
  ["Por que", "Suficiente para historia, dato fuerte y cierre sin perder velocidad"]
];

const attentionScores = [
  ["Curiosidad", 94, "Pregunta abierta con promesa especifica"],
  ["Sorpresa", 86, "Dato fuerte sin exagerar"],
  ["Emocion", 82, "Alivio y aspiracion"],
  ["Humor", 58, "Ligero, secundario"],
  ["Utilidad", 96, "Aplicable de inmediato"],
  ["Misterio", 81, "Sostiene el primer tercio"],
  ["Impacto visual", 87, "Antes/despues y micro escenas"],
  ["Potencial de conversacion", 90, "Pregunta final accionable"],
  ["Potencial de compartir", 88, "Tema util para pymes"]
];

const retentionRows = [
  ["Segundo 0", "Promesa clara", "Bajo", "Abrir con resultado concreto"],
  ["Segundo 3", "Curiosidad activa", "Bajo", "Mostrar problema reconocible"],
  ["Segundo 7", "Riesgo de explicacion lenta", "Medio", "Cortar directo a ejemplo"],
  ["Segundo 15", "Dato fuerte", "Bajo", "Usar numero visual grande"],
  ["Segundo 25", "Puede caer ritmo", "Medio", "Introducir giro narrativo"],
  ["Segundo 40", "Cierre conversable", "Bajo", "Pregunta simple sin pedir engagement falso"],
  ["Final", "Recordacion", "Bajo", "Logo discreto y valor resumido"]
];

const memoryRows = [
  ["Hooks mas efectivos", "Pregunta misteriosa + beneficio claro", "+18% retencion inicial"],
  ["Duraciones ideales", "20-45s para Shorts/Reels/TikTok", "+12% finalizacion"],
  ["Estilos visuales", "Documental hiperrealista corto", "+9% tiempo visto"],
  ["Velocidad de narracion", "Rapida pero con pausas en datos", "+7% claridad"],
  ["Tipo de musica", "Pulso suave, no protagonista", "+6% comodidad"],
  ["Colores", "Azul profundo + verde energia", "+5% identidad"],
  ["Ritmo de edicion", "Corte cada 2.8s en primeros 12s", "+11% retencion"],
  ["Tipo de personaje", "Persona creible, no celebridad", "+14% confianza"],
  ["Tipo de escenario", "Espacio real de trabajo", "+8% relevancia"],
  ["CTA mas efectivo", "Pregunta especifica y suave", "+16% comentarios"]
];

const channelMemoryRows = [
  ["Canal Ciencia", "42s", "Este dato parece mentira...", "Narrador claro", "13:00", "Edicion pausada"],
  ["Canal Curiosidades", "28s", "Nadie te cuenta esto...", "Narradora intrigante", "21:00", "Cortes rapidos"],
  ["AI Finance Daily", "38s", "La razon por la que...", "Experto sobrio", "08:00", "Graficos limpios"],
  ["Futuro Latino IA", "35s", "Esto esta pasando...", "Cercano LATAM", "17:00", "Energia alta"]
];

const countryMemoryRows = [
  ["Chile", "IA practica y ahorro", "32-45s", "21:00", "Media", "Humor seco", "Cercana"],
  ["Mexico", "Emprendimiento e IA", "28-42s", "13:00", "Alta", "Conversacional", "Energetica"],
  ["Brasil", "Energia y negocios", "35-50s", "17:00", "Media", "Optimista", "Clara"],
  ["Estados Unidos", "Productividad AI", "25-40s", "08:00", "Alta", "Directo", "Experta"],
  ["Espana", "Cultura y tecnologia", "30-48s", "20:00", "Media", "Ironico suave", "Editorial"],
  ["Japon", "Futuro y precision", "20-35s", "19:00", "Alta", "Sutil", "Serena"],
  ["Francia", "Viajes y estilo", "35-55s", "18:00", "Media", "Elegante", "Documental"],
  ["Alemania", "Productividad B2B", "45-70s", "08:00", "Media-alta", "Minimo", "Tecnica"]
];

const languageMemoryRows = [
  ["Espanol", "Hook emocional + utilidad", "Conversacional", "Comentarios altos"],
  ["Ingles", "Resultado directo", "Preciso", "Monetizacion alta"],
  ["Portugues", "Beneficio cotidiano", "Optimista", "Compartidos altos"],
  ["Frances", "Estetica + contexto", "Editorial", "Retencion media-alta"],
  ["Italiano", "Historia breve", "Calido", "Curiosidad alta"],
  ["Aleman", "Dato probado", "Claro y tecnico", "Confianza alta"],
  ["Japones", "Precision y calma", "Sereno", "Finalizacion alta"],
  ["Coreano", "Tendencia rapida", "Dinamico", "Enganche alto"],
  ["Arabe", "Contexto y valor", "Formal cercano", "Crecimiento alto"]
];

const experimentRows = [
  ["Video A", "Hook A", "38s", "Documental", "76% finalizacion", "Ganador parcial"],
  ["Video B", "Hook B", "28s", "Noticias rapidas", "69% finalizacion", "Mejor CTR"],
  ["Video C", "Hook C", "45s", "Storytelling emocional", "81% finalizacion", "Ganador"],
  ["Video D", "Hook D", "22s", "Minimalista", "63% finalizacion", "Descartar"]
];

const evolutionRows = [
  ["Introducciones largas estan perdiendo retencion", "Reducir apertura a menos de 3 segundos", "Alta"],
  ["Los personajes generan mayor atencion", "Agregar personaje creible en nichos educativos", "Media-alta"],
  ["Formato documental aumento tiempo de visualizacion", "Priorizarlo en paises con retencion alta", "Alta"],
  ["Narracion rapida funciona mejor en este nicho", "Subir ritmo sin perder claridad", "Media"],
  ["Preguntas especificas superan CTAs genericos", "Usar CTA conversacional, no pedir engagement falso", "Alta"]
];

const knowledgeRows = [
  ["Videos analizados", "128.420", "Patrones, no copias"],
  ["Ideas generadas", "42.860", "Angulos originales"],
  ["Guiones creados", "18.240", "Versionados"],
  ["Hooks probados", "9.814", "Comparacion A/B/C"],
  ["Estilos visuales", "186", "Preferencias por nicho"],
  ["Escenarios", "742", "Contextos seguros"],
  ["Narradores", "96", "Tono por idioma"],
  ["Formatos", "54", "Shorts, Reels, TikTok"],
  ["Paises", "38", "Memoria local"],
  ["Idiomas", "9", "Aprendizaje independiente"]
];

const selfImprovementRows = [
  ["Que mejoro hoy", "Detecto que los cierres con pregunta concreta suben comentarios"],
  ["Que descubrio", "Los hooks de misterio funcionan mejor si prometen utilidad real"],
  ["Que cambio", "Redujo duracion recomendada en videos de herramientas IA"],
  ["Que dejo de recomendar", "Intros explicativas largas antes del dato fuerte"],
  ["Nueva estrategia", "Personaje + escenario real + dato visual en los primeros 7s"]
];

const nextBestActions = [
  ["Cambiar hook", "Futuro Latino IA", "Usar pregunta mas especifica", "Impacto alto"],
  ["Reducir duracion", "AI Finance Daily", "Bajar de 52s a 39s", "Retencion"],
  ["Cambiar narrador", "Canal Ciencia", "Voz mas clara y menos dramatica", "Confianza"],
  ["Cambiar estilo", "Brasil Solar News", "Documental practico", "Tiempo visto"],
  ["Crear canal nuevo", "Mexico", "IA para pymes", "Oportunidad"],
  ["Cambiar horario", "Europe Travel Pulse", "Mover a 18:00 local", "Alcance"]
];

const learningMapRows = [
  ["Mexico", "Hooks conversacionales", "Transfiere a Chile y Colombia"],
  ["Brasil", "Utilidad cotidiana", "Transfiere a Portugal"],
  ["Estados Unidos", "Monetizacion SaaS", "Transfiere a Alemania"],
  ["Japon", "Retencion por precision", "Transfiere a Corea"],
  ["Francia", "Estetica documental", "Transfiere a Italia y Espana"]
];

const factoryStats = [
  ["Videos en produccion", "1.284", "Trend -> Render", "ok"],
  ["Videos renderizando", "312", "Render farm activa", "warn"],
  ["Esperando revision", "146", "Quality Gate", "info"],
  ["Programados", "2.408", "24 zonas horarias", "ok"],
  ["Publicados", "8.912", "Ultimas 24h", "ok"],
  ["Videos aprendiendo", "6.704", "Learning Engine", "info"],
  ["Canales activos", "480", "38 paises", "ok"],
  ["IA trabajando", "97%", "11 agentes", "ok"]
];

const e2eStages = [
  ["Idea", "Listo", "00:20", "Trend AI"],
  ["Opportunity Score", "Listo", "00:18", "Global Intelligence"],
  ["Editorial Director", "Listo", "00:35", "Editorial AI"],
  ["Story Director", "Listo", "00:42", "Story AI"],
  ["Hook Builder", "Listo", "00:28", "Hook AI"],
  ["Storyboard", "En curso", "01:20", "Scene AI"],
  ["Voice Selection", "En curso", "00:30", "Voice AI"],
  ["Scene Builder", "Pendiente", "01:45", "Scene AI"],
  ["Video Generation", "Pendiente", "04:20", "Render AI"],
  ["Music", "Pendiente", "00:40", "Audio AI"],
  ["Subtitles", "Pendiente", "00:55", "Subtitle AI"],
  ["Quality Check", "Pendiente", "01:05", "Quality AI"],
  ["Publishing Queue", "Pendiente", "00:25", "Publish AI"],
  ["Published", "Pendiente", "API mock", "Publish AI"],
  ["Analytics", "Pendiente", "24h", "Analytics AI"],
  ["Learning Engine", "Pendiente", "Continuo", "Learning AI"]
];

const liveFactoryRows = [
  ["Video 001", "Renderizando", 67, "Render AI", "Mexico / Espanol"],
  ["Video 002", "Narracion", 44, "Voice AI", "US / Ingles"],
  ["Video 003", "Subtitulos", 58, "Subtitle AI", "Brasil / Portugues"],
  ["Video 004", "Programado", 91, "Publish AI", "Francia / Frances"],
  ["Video 005", "Publicado", 100, "Analytics AI", "Alemania / Aleman"],
  ["Video 006", "Aprendiendo", 82, "Learning AI", "Italia / Italiano"]
];

const workerRows = [
  ["Trend AI", "82%", "Analizando oportunidades", "18h 42m"],
  ["Research AI", "64%", "Validando contexto", "17h 10m"],
  ["Editorial AI", "71%", "Priorizando ideas", "19h 05m"],
  ["Story AI", "76%", "Definiendo emocion", "15h 22m"],
  ["Script AI", "69%", "Versionando guion", "14h 58m"],
  ["Voice AI", "88%", "Generando narracion", "13h 16m"],
  ["Scene AI", "73%", "Construyendo escenas", "12h 40m"],
  ["Subtitle AI", "51%", "Sincronizando texto", "16h 08m"],
  ["Render AI", "93%", "Render 9:16", "20h 31m"],
  ["Publish AI", "48%", "Cola programada", "11h 27m"],
  ["Learning AI", "79%", "Actualizando principios", "21h 03m"]
];

const factoryChannels = [
  ["Canal Ciencia", "Espanol", "Chile", "8", "Activo", "$12.4K"],
  ["Canal Curiosidades", "Espanol", "Mexico", "12", "Activo", "$18.7K"],
  ["Canal Tecnologia", "Ingles", "Estados Unidos", "16", "Activo", "$42.1K"],
  ["Canal Historia", "Frances", "Francia", "6", "Revision", "$8.9K"],
  ["Canal Salud", "Portugues", "Brasil", "8", "Activo", "$13.3K"],
  ["Canal Viajes", "Italiano", "Italia", "10", "Activo", "$10.8K"],
  ["Canal Economia", "Aleman", "Alemania", "8", "Activo", "$16.2K"],
  ["Canal Futuro", "Japones", "Japon", "6", "Activo", "$11.9K"]
];

const schedulerRows = [
  ["America/Santiago", "Chile", "Espanol", "21:00", "184", "96"],
  ["America/Mexico_City", "Mexico", "Espanol", "13:00", "312", "188"],
  ["America/New_York", "Estados Unidos", "Ingles", "08:00", "420", "302"],
  ["America/Sao_Paulo", "Brasil", "Portugues", "17:00", "244", "166"],
  ["Europe/Paris", "Francia", "Frances", "18:00", "138", "84"],
  ["Europe/Berlin", "Alemania", "Aleman", "08:00", "126", "77"],
  ["Asia/Tokyo", "Japon", "Japones", "19:00", "118", "62"]
];

const factoryMoneyRows = [
  ["RPM promedio", "$5.84", "+8.2%"],
  ["CPM promedio", "$11.40", "+6.1%"],
  ["Ingresos diarios", "$286K", "+11.8%"],
  ["Ingresos mensuales", "$8.4M", "+19.4%"],
  ["Canal mas rentable", "AI Finance Daily", "$42.8K"],
  ["Video top", "IA para pymes", "8.4M views"]
];

const journeyRows = [
  ["Idea", "IA para recuperar tiempo en pymes", "Trend AI detecto oportunidad"],
  ["Investigacion", "Fuentes permitidas", "Research AI valido contexto"],
  ["Guion", "42 segundos", "Script AI creo version original"],
  ["Storyboard", "9 escenas", "Story AI definio ritmo"],
  ["Escenas", "Oficina realista", "Scene AI preparo ambiente"],
  ["Narracion", "Espanol LATAM", "Voice AI eligio tono cercano"],
  ["Subtitulos", "Cortes cortos", "Subtitle AI sincronizo"],
  ["Render", "9:16 premium", "Render AI completo version"],
  ["Programacion", "13:00 Mexico", "Scheduler AI eligio ventana"],
  ["Publicado", "API mock", "Publish AI simulado"],
  ["Analitica", "Retencion 81%", "Analytics AI midio"],
  ["Aprendizaje", "Hook conversable", "Learning AI guardo principio"]
];

const executiveRows = [
  ["Canales", "480", "+32 mes"],
  ["Videos", "8.912", "24h"],
  ["Ingresos", "$286K", "dia"],
  ["Costos IA", "$18.7K", "dia"],
  ["Tiempo promedio", "38s", "video corto"],
  ["Rendimiento", "+22.4%", "views"],
  ["Paises", "38", "activos"],
  ["Idiomas", "9", "aprendiendo"],
  ["Servidores", "99.97%", "operativo"],
  ["Estado IA", "97%", "trabajando"],
  ["Alertas", "4", "moderadas"],
  ["Objetivos del dia", "84%", "completado"]
];

const confidenceRows = [
  ["Opportunity Fit", 94, "Pais, idioma y nicho alineados"],
  ["Editorial Safety", 97, "Sin rumor ni copia"],
  ["Retention Forecast", 88, "Hook y ritmo fuertes"],
  ["Monetization Fit", 81, "Nicho comercial sano"]
];

const view = document.getElementById("view");
function learningManifesto() {
  return `<article class="card learning-manifesto"><span class="eyebrow">Learning & Evolution Engine</span><h3>La inteligencia no consiste en producir mas videos. Consiste en aprender continuamente como producir mejores videos.</h3><p>La IA no memoriza videos, guiones, personajes ni formatos exactos. Memoriza principios generales: que retiene, que ayuda, que entretiene, que conversa y que debe dejar de recomendar.</p><div class="guardrail-list"><span>Memoria de principios</span><span>No copiar contenido</span><span>Aprendizaje por canal</span><span>Evolucion continua</span></div></article>`;
}

function memoryCard([label, value, note]) {
  return `<article class="card memory-card"><span class="eyebrow">Memoria</span><h3>${label}</h3><strong>${value}</strong><p>${note}</p></article>`;
}

function learningEngine() {
  return `${learningManifesto()}<div class="grid two"><article class="card"><h3>Cerebro evolutivo global</h3><p class="muted">La plataforma compara resultados simulados y ajusta principios creativos por canal, pais, idioma y nicho.</p>${selfImprovementRows.map(([label, value]) => `<div class="entity-row"><div><span class="entity-title">${label}</span><span class="entity-meta">${value}</span></div>${badge("Aprendido", "ok")}</div>`).join("")}</article>${learningMap(true)}</div>${globalKnowledge(true)}`;
}

function memoryEngine() {
  return `${learningManifesto()}<div class="grid four">${memoryRows.map(memoryCard).join("")}</div>`;
}

function channelMemory() {
  return `${learningManifesto()}${table(["Canal", "Mejor duracion", "Mejor hook", "Mejor narrador", "Mejor horario", "Mejor ritmo"], channelMemoryRows)}`;
}

function countryMemory() {
  return `${learningManifesto()}${table(["Pais", "Temas favoritos", "Duraciones", "Horario ideal", "Competencia", "Humor", "Narracion"], countryMemoryRows)}`;
}

function languageMemory() {
  return `${learningManifesto()}<div class="style-lab-grid">${languageMemoryRows.map(([language, pattern, tone, result]) => `<article class="card style-card"><span class="eyebrow">Idioma</span><h3>${language}</h3><p>${pattern}</p><div class="style-meta"><span>Tono: ${tone}</span><span>${result}</span></div></article>`).join("")}</div>`;
}

function experimentEngine() {
  return `${learningManifesto()}<article class="card"><span class="eyebrow">Experiment Engine</span><h3>La IA experimenta y compara. Nunca se queda con una sola estrategia.</h3><div class="experiment-grid">${experimentRows.map(([video, hook, duration, style, result, state]) => `<article class="experiment-card"><span>${video}</span><h3>${hook}</h3><p>${duration} · ${style}</p><strong>${result}</strong>${badge(state, state.includes("Ganador") ? "ok" : state.includes("Descartar") ? "warn" : "info")}</article>`).join("")}</div></article>`;
}

function creativeEvolution() {
  return `${learningManifesto()}<article class="card"><span class="eyebrow">Creative Evolution</span><h3>Recomendaciones automaticas simuladas</h3>${evolutionRows.map(([finding, recommendation, impact]) => `<div class="entity-row"><div><span class="entity-title">${finding}</span><span class="entity-meta">${recommendation}</span></div>${badge(impact, impact === "Alta" ? "ok" : "info")}</div>`).join("")}</article>`;
}

function globalKnowledge(compact = false) {
  const panel = `<article class="card"><span class="eyebrow">Global Knowledge</span><h3>Conocimiento acumulado de principios creativos</h3><div class="knowledge-grid">${knowledgeRows.map(([label, value, note]) => `<article><strong>${value}</strong><span>${label}</span><small>${note}</small></article>`).join("")}</div></article>`;
  return compact ? panel : `${learningManifesto()}${panel}`;
}

function aiSelfImprovement() {
  return `${learningManifesto()}<article class="card"><span class="eyebrow">AI Self Improvement</span><h3>Lo que la IA mejoro hoy</h3>${selfImprovementRows.map(([label, value]) => `<div class="director-row"><span>${label}</span><strong>${value}</strong>${badge("Evolucion", "ok")}</div>`).join("")}</article>`;
}

function learningMap(compact = false) {
  const panel = `<article class="card heatmap-card"><span class="eyebrow">Global Learning Map</span><h3>Transferencia mundial de conocimiento</h3><div class="heatmap-world learning-world"><span class="heat h1"></span><span class="heat h2"></span><span class="heat h3"></span><span class="heat h4"></span><span class="heat h5"></span><span class="heat h6"></span><i class="heat-line l1"></i><i class="heat-line l2"></i><i class="heat-line l3"></i><b>LEARNING GRID</b></div>${table(["Pais", "Que aprende", "Transferencia"], learningMapRows)}</article>`;
  return compact ? panel : `${learningManifesto()}${panel}`;
}

function nextBestAction() {
  return `${learningManifesto()}<article class="card"><span class="eyebrow">Next Best Action</span><h3>Que deberia hacer ahora la plataforma?</h3><div class="next-action-grid">${nextBestActions.map(([action, target, reason, impact], index) => `<article class="next-action"><span>${String(index + 1).padStart(2, "0")}</span><h3>${action}</h3><p>${target}</p><strong>${reason}</strong>${badge(impact, impact === "Oportunidad" || impact === "Retencion" ? "ok" : "info")}</article>`).join("")}</div></article>`;
}
function storyDirector() {
  return `${intelligenceManifesto()}<div class="grid two"><article class="card director-panel"><span class="eyebrow">Story Director AI</span><h3>La IA no piensa en videos. Piensa en personas.</h3>${storyDirectorRows.map(([label, value], index) => `<div class="director-row"><span>${label}</span><strong>${value}</strong>${index === storyDirectorRows.length - 1 ? badge("Producir", "ok") : ""}</div>`).join("")}</article><article class="card"><span class="eyebrow">Intensidad narrativa</span><h3>Controles creativos recomendados</h3>${scoreGrid(storyLevels)}</article></div>`;
}

function videoStyleLab() {
  return `${intelligenceManifesto()}<div class="style-lab-grid">${styleLabRows.map(([style, attention, retention, cost, time, complexity]) => `<article class="card style-card"><span class="eyebrow">Estilo</span><h3>${style}</h3><div class="mini-score"><span>Atencion</span><strong>${attention}</strong><div class="progress-track"><div class="progress-fill" style="width:${attention}%"></div></div></div><div class="mini-score"><span>Retencion</span><strong>${retention}</strong><div class="progress-track"><div class="progress-fill" style="width:${retention}%"></div></div></div><div class="style-meta"><span>Costo: ${cost}</span><span>Tiempo: ${time}</span><span>Complejidad: ${complexity}</span></div></article>`).join("")}</div>`;
}

function characterSceneBuilder() {
  return `${intelligenceManifesto()}<article class="card"><span class="eyebrow">Character & Scene Builder</span><h3>Diseno visual del personaje, camara y ambiente</h3><div class="scene-grid">${characterSceneRows.map(([label, value, note]) => `<article class="scene-card"><span>${label}</span><strong>${value}</strong><p>${note}</p></article>`).join("")}</div></article>`;
}

function hookRetentionSimulator() {
  return `${intelligenceManifesto()}<article class="card"><span class="eyebrow">Hook vs Retention Simulator</span><h3>Comparacion visual de hooks y permanencia</h3><div class="hook-compare">${hookRetentionRows.map(([name, hook, s3, s7, s15, finalRetention, share, comment, finish]) => `<article class="hook-sim"><span class="eyebrow">${name}</span><h3>${hook}</h3><div class="retention-bars"><label>S3 <i style="width:${s3}%"></i><b>${s3}%</b></label><label>S7 <i style="width:${s7}%"></i><b>${s7}%</b></label><label>S15 <i style="width:${s15}%"></i><b>${s15}%</b></label><label>Final <i style="width:${finalRetention}%"></i><b>${finalRetention}%</b></label></div><div class="grid three"><span>${badge(`Compartir ${share}%`, "info")}</span><span>${badge(`Comentar ${comment}%`, "ok")}</span><span>${badge(`Terminar ${finish}%`, "warn")}</span></div></article>`).join("")}</div></article>`;
}

function verticalBlueprint() {
  return `${intelligenceManifesto()}<article class="card"><span class="eyebrow">Vertical Video Blueprint</span><h3>Plano completo del video 9:16 antes de producir</h3><div class="blueprint-flow">${blueprintRows.map(([stage, time, narration, subtitles, music, camera], index) => `<div class="blueprint-step"><span>${String(index + 1).padStart(2, "0")}</span><strong>${stage}</strong><small>${time}</small><p><b>Narracion:</b> ${narration}</p><p><b>Subtitulos:</b> ${subtitles}</p><p><b>Musica/Efectos:</b> ${music}</p><p><b>Camara:</b> ${camera}</p></div>`).join("")}</div></article>`;
}

function smartDurationEngine() {
  return `${intelligenceManifesto()}<div class="grid two"><article class="card"><span class="eyebrow">Smart Duration Engine</span><h3>Decision automatica de duracion ideal</h3>${durationDecisionRows.map(([label, value], index) => `<div class="director-row"><span>${label}</span><strong>${value}</strong>${index === 9 ? badge("Elegida", "ok") : ""}</div>`).join("")}</article>${table(["Tipo", "Duracion", "Uso", "Prioridad"], durationRows.map(r => [r[0], r[1], r[2], badge(r[3], r[3].includes("TikTok") ? "ok" : "info")]))}</div>`;
}

function attentionEngine() {
  const total = Math.round(attentionScores.reduce((sum, item) => sum + item[1], 0) / attentionScores.length);
  return `${intelligenceManifesto()}<article class="card attention-hero"><span class="eyebrow">Attention Engine</span><h3>Score general de atencion: ${total}/100</h3><p>Este motor piensa solo en captar atencion de forma responsable: curiosidad, utilidad, misterio, impacto visual y conversacion real.</p></article>${scoreGrid(attentionScores)}`;
}

function retentionEngine() {
  return `${intelligenceManifesto()}<article class="card"><span class="eyebrow">Retention Engine</span><h3>Por que alguien seguiria viendo este video?</h3><div class="decision-timeline">${retentionRows.map(([time, moment, risk, recommendation]) => `<div class="timeline-item"><time>${time}</time><div><strong>${moment}</strong><p>Riesgo de abandono: ${risk}. Recomendacion: ${recommendation}.</p></div></div>`).join("")}</div></article>`;
}
const pageTitle = document.getElementById("pageTitle");
const sideNav = document.getElementById("sideNav");
const toast = document.getElementById("toast");
const sidebar = document.querySelector(".sidebar");

function badge(text, tone = "") { return `<span class="badge ${tone}">${text}</span>`; }
function toneFor(text) {
  if (["Activo", "OK", "Live", "Controlado", "Normal", "En expansion", "Alta traccion"].some(x => text.includes(x))) return "ok";
  if (["Hot"].some(x => text.includes(x))) return "hot";
  if (["Mock", "Pendiente", "Revision", "Alta", "Atencion", "Competitivo"].some(x => text.includes(x))) return "warn";
  return "info";
}
function table(headers, rows) {
  return `<article class="table-card"><table class="table"><thead><tr>${headers.map(h => `<th>${h}</th>`).join("")}</tr></thead><tbody>${rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join("")}</tr>`).join("")}</tbody></table></article>`;
}
function metricCards() {
  return `<div class="grid metrics">${metrics.map(([label, value, delta, tone]) => `<article class="card metric-card"><small>${label}</small><span class="metric-value">${value}</span><span class="delta ${tone === 'warn' ? 'warn' : ''}">${delta}</span></article>`).join("")}</div>`;
}
function statusPanel(title = "Global operations health") {
  return `<article class="card"><h3>${title}</h3>${statuses.map(([name, meta, state, tone]) => `<div class="status-row"><div><span class="status-name">${name}</span><span class="status-meta">${meta}</span></div>${badge(state, tone)}</div>`).join("")}</article>`;
}
function worldMap() {
  const points = [[17,38,""],[27,58,"green"],[43,34,""],[55,47,"green"],[67,36,"amber"],[76,55,""],[84,69,"green"],[36,22,"amber"]];
  const arcs = [[18,40,220,-10],[28,60,260,-22],[44,36,210,18],[57,49,180,-8],[68,38,150,24]];
  return `<article class="card world-panel"><span class="eyebrow">Mapa mundial de tendencias</span><h3>Red global de senales de contenido</h3><p class="muted">Nodos simulados por actividad de tendencia, idioma, pais, cola de render y monetizacion.</p><div class="world-map">${arcs.map(([x,y,w,r]) => `<i class="arc" style="left:${x}%;top:${y}%;width:${w}px;transform:rotate(${r}deg)"></i>`).join("")}${points.map(([x,y,t]) => `<span class="signal ${t}" style="left:${x}%;top:${y}%"></span>`).join("")}<span class="world-label">GLOBAL</span></div></article>`;
}
function barChart(title = "Rendimiento semanal global") {
  const bars = [[68,"Lun"],[83,"Mar"],[74,"Mie"],[91,"Jue"],[96,"Vie"],[62,"Sab"],[79,"Dom"]];
  return `<article class="card"><h3>${title}</h3><p class="muted">Views, publicaciones, eficiencia de agentes y monetizacion simulada.</p><div class="chart-bars">${bars.map(([h,d]) => `<div class="bar" style="height:${h}%"><span>${d}</span></div>`).join("")}</div></article>`;
}
function scoreMeter(label, score, note, inverted = false) {
  const tone = inverted ? (score <= 25 ? "ok" : score <= 55 ? "warn" : "hot") : (score >= 86 ? "ok" : score >= 70 ? "info" : "warn");
  return `<article class="card score-card"><div class="score-head"><div><span class="eyebrow">${label}</span><strong>${score}</strong></div>${badge(tone === "ok" ? "Fuerte" : tone === "info" ? "Bueno" : "Revision", tone)}</div><div class="progress-track"><div class="progress-fill" style="width:${score}%"></div></div><p class="muted">${note}</p></article>`;
}

function scoreGrid(rows, invertedLabel = "") {
  return `<div class="grid four">${rows.map(([label, score, note]) => scoreMeter(label, score, note, label === invertedLabel)).join("")}</div>`;
}

function contentMission() {
  return `<article class="card content-mission"><span class="eyebrow">Content Quality Philosophy</span><h3>No producir videos genericos. Producir contenido que la gente quiera terminar, comentar y compartir.</h3><p>El prototipo modela un motor editorial responsable: curiosidad, sorpresa, utilidad, emocion y conversacion, sin rumores, sin copiar virales y sin manipular algoritmos.</p><div class="guardrail-list">${guardrailRows.map(item => `<span>${item}</span>`).join("")}</div></article>`;
}

function viralPsychology() {
  return `${contentMission()}${scoreGrid(viralFactors)}<div class="grid two"><article class="card"><h3>Lectura editorial simulada</h3><p>La idea tiene alta retencion porque combina una pregunta inicial clara, utilidad real y una promesa que se puede cumplir dentro del video.</p><p class="muted">El sistema visualiza factores de atraccion humana sin convertirlos en manipulacion. La meta es entretenimiento responsable.</p></article>${qualityGate(true)}</div>`;
}

function channelDna() {
  return `${contentMission()}${table(["Canal", "Personalidad", "Tono", "Publico", "Profundidad", "Visual", "Narrador", "Duracion", "Hook favorito", "Prohibidos", "Recomendados"], channelDnaRows.map(row => [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], badge(row[9], "warn"), badge(row[10], "ok")]))}`;
}

function qualityGate(compact = false) {
  const body = `<article class="card"><span class="eyebrow">Content Quality Gate</span><h3>Revision previa antes de aprobar un video</h3>${qualityChecks.map(([check, state, note]) => `<div class="status-row"><div><span class="status-name">${check}</span><span class="status-meta">${note}</span></div>${badge(state, state === "Aprobado" ? "ok" : "warn")}</div>`).join("")}</article>`;
  return compact ? body : `${contentMission()}${body}`;
}

function entertainmentScoring() {
  return `${contentMission()}${scoreGrid(entertainmentScores, "Riesgo de baja calidad")}<article class="card"><h3>Resultado simulado</h3><p>La idea puede pasar a laboratorio creativo porque combina claridad, conversacion y valor real. El riesgo de baja calidad permanece bajo mientras se mantengan fuentes verificadas y localizacion cultural.</p></article>`;
}

function ideaLab() {
  return `${contentMission()}<article class="card"><span class="eyebrow">Idea Lab</span><h3>Versiones creativas antes de producir</h3><p class="muted">El laboratorio transforma una premisa base en angulos mas entretenidos, emocionales, educativos o cortos, manteniendo seguridad editorial.</p>${ideaLabRows.map(([type, idea]) => `<div class="entity-row"><div><span class="entity-title">${type}</span><span class="entity-meta">${idea}</span></div>${badge(type.includes("polemica") ? "Segura" : "Mock", type.includes("polemica") ? "warn" : "info")}</div>`).join("")}</article>`;
}

function hookBuilder() {
  return `${contentMission()}${table(["Hook", "Score", "Uso recomendado", "Regla responsable"], hookRows.map(r => [r[0], r[1], r[2], r[3]]))}<article class="card"><h3>Comparador visual de hooks</h3><div class="hook-stack">${hookRows.map(([hook, score]) => `<div class="hook-card"><strong>${hook}</strong><span>${score}/100</span></div>`).join("")}</div></article>`;
}

function curiosityMap() {
  return `${worldMap()}${table(["Pais", "Idioma", "Nicho", "Tema que atrae", "Motor emocional", "Potencial"], curiosityRows.map(r => [r[0], r[1], r[2], r[3], r[4], badge(r[5], toneFor(r[5]))]))}`;
}
function intelligenceManifesto() {
  return `<article class="card intelligence-manifesto"><span class="eyebrow">Global Intelligence Engine</span><h3>No seguimos tendencias. Detectamos oportunidades antes que los demas.</h3><p>El cerebro editorial simulado cruza pais, idioma, nicho, competencia, demanda, calidad, riesgo y ventana horaria antes de recomendar producir un video.</p><div class="guardrail-list"><span>Razonar antes de producir</span><span>Contenido original</span><span>Oportunidad antes que volumen</span><span>Seguridad editorial</span></div></article>`;
}

function radarRings() {
  return `<article class="card radar-card"><span class="eyebrow">Opportunity Radar</span><h3>Radar mundial de oportunidad editorial</h3><div class="radar"><span class="ring r1"></span><span class="ring r2"></span><span class="ring r3"></span><span class="sweep"></span>${opportunityRows.map((row, index) => `<i class="radar-dot d${index}"><b>${row[0].slice(0, 2).toUpperCase()}</b></i>`).join("")}</div></article>`;
}

function globalIntelligence() {
  return `${intelligenceManifesto()}<div class="grid two">${radarRings()}${editorialDirector(true)}</div><div class="grid two">${globalContentHeatmap(true)}${qualityDashboard(true)}</div>`;
}

function opportunityRadar() {
  return `${intelligenceManifesto()}<div class="grid two">${radarRings()}${table(["Pais", "Nicho emergente", "Idioma", "Competencia", "Demanda", "Ventanas", "Score"], opportunityRows.map(r => [r[0], r[1], r[2], badge(r[3], r[3] === "Baja" ? "ok" : "warn"), badge(r[4], "ok"), r[5], `${r[6]}/100`]))}</div>`;
}

function competitorIntelligence() {
  return `${intelligenceManifesto()}<article class="card"><span class="eyebrow">Competitor Intelligence</span><h3>Aprender del mercado sin copiar contenido</h3><p class="muted">Este modulo visual identifica patrones generales y oportunidades. La plataforma debe generar guiones, hooks y estructuras originales.</p>${competitorInsights.map(([label, insight, rule]) => `<div class="entity-row"><div><span class="entity-title">${label}: ${insight}</span><span class="entity-meta">${rule}</span></div>${badge("Original only", "ok")}</div>`).join("")}</article>`;
}

function contentPipeline() {
  return `${intelligenceManifesto()}<article class="card"><span class="eyebrow">Content Pipeline</span><h3>Recorrido completo de una oportunidad hasta analitica</h3><div class="pipeline-flow">${pipelineStages.map(([stage, state, time, owner], index) => `<div class="flow-step"><span class="flow-index">${String(index + 1).padStart(2, "0")}</span><strong>${stage}</strong><small>${owner}</small><div>${badge(state, state === "Listo" ? "ok" : state === "En curso" ? "info" : "warn")}<em>${time}</em></div></div>`).join("")}</div></article>`;
}

function editorialDirector(compact = false) {
  const panel = `<article class="card director-panel"><span class="eyebrow">Editorial Director AI</span><h3>Por que recomendamos producir este contenido</h3>${editorialRecommendation.map(([label, value], index) => `<div class="director-row"><span>${label}</span><strong>${value}</strong>${index === editorialRecommendation.length - 1 ? badge("Recomendado", "ok") : ""}</div>`).join("")}</article>`;
  return compact ? panel : `${intelligenceManifesto()}${panel}`;
}

function globalContentHeatmap(compact = false) {
  const panel = `<article class="card heatmap-card"><span class="eyebrow">Global Content Heatmap</span><h3>Paises, idiomas, canales y produccion activa</h3><div class="heatmap-world"><span class="heat h1"></span><span class="heat h2"></span><span class="heat h3"></span><span class="heat h4"></span><span class="heat h5"></span><span class="heat h6"></span><i class="heat-line l1"></i><i class="heat-line l2"></i><i class="heat-line l3"></i><b>ACTIVE CONTENT GRID</b></div><div class="grid four"><article><strong>38</strong><span>Paises activos</span></article><article><strong>6</strong><span>Idiomas activos</span></article><article><strong>248</strong><span>Canales activos</span></article><article><strong>684</strong><span>Produccion en curso</span></article></div></article>`;
  return compact ? panel : `${intelligenceManifesto()}${panel}`;
}

function aiDecisionTimeline() {
  return `${intelligenceManifesto()}<article class="card"><span class="eyebrow">AI Decision Timeline</span><h3>Cronologia de decisiones editoriales simuladas</h3><div class="decision-timeline">${decisionTimeline.map(([time, title, detail]) => `<div class="timeline-item"><time>${time}</time><div><strong>${title}</strong><p>${detail}</p></div></div>`).join("")}</div></article>`;
}

function qualityDashboard(compact = false) {
  const panel = `<article class="card"><span class="eyebrow">Quality Dashboard</span><h3>Indicadores de calidad antes de publicar</h3>${scoreGrid(qualityDashboardScores)}</article>`;
  return compact ? panel : `${intelligenceManifesto()}${panel}`;
}
function aiConfidencePanel() {
  const average = Math.round(confidenceRows.reduce((sum, item) => sum + item[1], 0) / confidenceRows.length);
  return `<article class="card confidence-panel"><span class="eyebrow">AI Confidence Score</span><h3>${average}/100 antes de producir</h3><p>La IA muestra su nivel de seguridad editorial, creativa y operativa antes de activar la fabrica de contenido.</p>${scoreGrid(confidenceRows)}</article>`;
}

function factoryManifesto() {
  return `<article class="card factory-manifesto"><span class="eyebrow">Digital Content Factory</span><h3>No automatizamos videos. Automatizamos la creacion inteligente de contenido.</h3><p>La fabrica visual simula una operacion mundial 24/7: oportunidades, direccion editorial, estilo, render, programacion, analitica y aprendizaje continuo.</p><div class="guardrail-list"><span>Mock data</span><span>Sin publicacion real</span><span>Sin workers reales</span><span>Operacion visual 24/7</span></div></article>`;
}

function factoryMetricCards() {
  return `<div class="grid metrics">${factoryStats.map(([label, value, delta, tone]) => `<article class="card metric-card"><small>${label}</small><span class="metric-value">${value}</span><span class="delta ${tone === "warn" ? "warn" : ""}">${delta}</span></article>`).join("")}</div>`;
}

function digitalFactory() {
  return `${factoryManifesto()}${aiConfidencePanel()}<div class="grid two">${factoryActivity()}${queueView("Fabrica mundial en movimiento")}</div>${factoryMetricCards()}`;
}

function factoryActivity() {
  return `<article class="card factory-activity"><span class="eyebrow">Global Factory</span><h3>Actividad simulada en tiempo real</h3><div class="factory-pulse"><span></span><span></span><span></span><span></span><span></span></div>${liveFactoryRows.map(([video, state, progress, ai, region]) => `<div class="queue-row"><div><span class="entity-title">${video} · ${state}</span><span class="entity-meta">${ai} · ${region}</span><div class="progress-track"><div class="progress-fill" style="width:${progress}%"></div></div></div>${badge(`${progress}%`, progress > 80 ? "ok" : "info")}</div>`).join("")}</article>`;
}

function globalFactory() {
  return `${factoryManifesto()}${factoryMetricCards()}<div class="grid two">${factoryActivity()}${statusPanel("Estado global de la fabrica")}</div>`;
}

function endToEndPipeline() {
  return `${factoryManifesto()}${aiConfidencePanel()}<article class="card"><span class="eyebrow">End to End Pipeline</span><h3>Recorrido completo desde idea hasta aprendizaje</h3><div class="pipeline-flow factory-flow">${e2eStages.map(([stage, state, time, owner], index) => `<div class="flow-step"><span class="flow-index">${String(index + 1).padStart(2, "0")}</span><strong>${stage}</strong><small>${owner}</small><div>${badge(state, state === "Listo" ? "ok" : state === "En curso" ? "info" : "warn")}<em>${time}</em></div></div>`).join("")}</div></article>`;
}

function videoFactoryLive() {
  return `${factoryManifesto()}${factoryActivity()}`;
}

function aiWorkers() {
  return `${factoryManifesto()}<div class="worker-grid">${workerRows.map(([name, cpu, task, uptime]) => `<article class="card worker-card"><span class="eyebrow">AI Worker</span><h3>${name}</h3><strong>${cpu}</strong><div class="progress-track"><div class="progress-fill" style="width:${cpu.replace("%", "")}%"></div></div><p>${task}</p>${badge(`Activo ${uptime}`, "ok")}</article>`).join("")}</div>`;
}

function multiChannelManager() {
  return `${factoryManifesto()}${table(["Canal", "Idioma", "Pais", "Videos diarios", "Estado", "Ingresos simulados"], factoryChannels.map(r => [r[0], r[1], r[2], r[3], badge(r[4], r[4] === "Activo" ? "ok" : "warn"), r[5]]))}`;
}

function worldSchedulerFactory() {
  return `${factoryManifesto()}${table(["Zona horaria", "Pais", "Idioma", "Hora ideal", "Pendientes", "Publicados"], schedulerRows)}`;
}

function factoryMonetization() {
  return `${factoryManifesto()}<div class="grid metrics">${factoryMoneyRows.map(([label, value, delta]) => `<article class="card metric-card"><small>${label}</small><span class="metric-value">${value}</span><span class="delta">${delta}</span></article>`).join("")}</div>${table(["Canal", "Pais", "Views", "Ingresos"], channelRows.map(r => [r[0], r[1], r[5], r[6]]))}`;
}

function missionControl() {
  return `${factoryManifesto()}${aiConfidencePanel()}<div class="grid two">${globalContentHeatmap(true)}${factoryActivity()}</div>${factoryMetricCards()}<div class="grid three"><article class="card"><h3>Opportunity Radar</h3><p class="muted">38 paises activos, 12 nichos emergentes, 4 alertas moderadas.</p>${badge("Oportunidad alta", "ok")}</article><article class="card"><h3>Learning Engine</h3><p class="muted">6.704 videos alimentando principios creativos simulados.</p>${badge("Evolucionando", "info")}</article><article class="card"><h3>Quality Score</h3><p class="muted">Originalidad, seguridad y retencion sobre umbral.</p>${badge("94/100", "ok")}</article></div>`;
}

function fullVideoJourney() {
  return `${factoryManifesto()}<article class="card"><span class="eyebrow">Full Video Journey</span><h3>Video ficticio 001 · IA para recuperar tiempo en pymes</h3><div class="decision-timeline">${journeyRows.map(([stage, value, detail]) => `<div class="timeline-item"><time>${stage}</time><div><strong>${value}</strong><p>${detail}</p></div></div>`).join("")}</div></article>`;
}

function executiveOverview() {
  return `${factoryManifesto()}<div class="grid metrics">${executiveRows.map(([label, value, delta]) => `<article class="card metric-card"><small>${label}</small><span class="metric-value">${value}</span><span class="delta">${delta}</span></article>`).join("")}</div><div class="grid two">${statusPanel("Estado ejecutivo")}${nextBestAction()}</div>`;
}

function pipeline() {
  const steps = [["Trend Scan","392 senales","ok"],["Research","218 fuentes","ok"],["Scripts","684 guiones","ok"],["Voice IA","421 audios","warn"],["Render","112 activos","warn"],["Publish","API mock","info"]];
  return `<article class="card"><span class="eyebrow">Centro de automatizacion</span><h3>Pipeline mundial 08:00 · 13:00 · 17:00 · 21:00</h3><div class="pipeline">${steps.map(([name, meta, tone]) => `<div class="pipeline-step">${badge(tone.toUpperCase(), tone)}<strong>${name}</strong><span class="muted">${meta}</span></div>`).join("")}</div></article>`;
}
function queueView(title = "Cola mundial de videos") {
  return `<article class="card"><h3>${title}</h3>${queueRows.map(([region, task, channel, progress, state]) => `<div class="queue-row"><div><span class="entity-title">${region} · ${task}</span><span class="entity-meta">${channel}</span><div class="progress-track"><div class="progress-fill" style="width:${progress}%"></div></div></div>${badge(state, progress > 80 ? "ok" : "warn")}</div>`).join("")}</article>`;
}
function login() {
  return `<div class="login-view"><section class="login-story"><span class="eyebrow">Global AI Video Operating System</span><h2>Una consola empresarial para controlar una red mundial de creacion de contenido IA.</h2><p class="muted">Vista simulada premium. La autenticacion real se implementara despues.</p></section><section class="login-panel"><span class="eyebrow">Secure Command Access</span><h3>Iniciar sesion</h3><div class="field"><label>Correo</label><input readonly value="admin@appfactorychile.com" /></div><div class="field"><label>Clave</label><input readonly value="********" /></div><button class="primary-btn" data-soon>Entrar</button><p class="muted" style="margin-top:14px">Botones en modo demostracion: Proximamente.</p></section></div>`;
}
function dashboard() {
  return `${metricCards()}${contentMission()}<div class="grid two">${worldMap()}${statusPanel("Estado global en tiempo real")}</div>${pipeline()}<div class="grid two">${barChart()}${queueView("Cola mundial critica")}</div>`;
}
function intelligence() {
  return `<div class="grid two">${worldMap()}${statusPanel("Centro de inteligencia global")}</div>${table(["Tendencia", "Pais", "Idioma", "Score", "Estado"], trendRows.map(r => [r[0], r[1], r[2], r[3], badge(r[4], toneFor(r[4]))]))}`;
}
function trends() { return `${worldMap()}${table(["Tendencia", "Pais", "Idioma", "Score", "Clasificacion"], trendRows.map(r => [r[0], r[1], r[2], r[3], badge(r[4], toneFor(r[4]))]))}`; }
function byCountry() { return table(["Pais", "Idioma", "Nicho dominante", "Videos", "Views 24h", "Ingresos", "Estado"], countryRows.map(r => [...r.slice(0,6), badge(r[6], toneFor(r[6]))])); }
function byLanguage() { return table(["Idioma", "Canales", "Videos", "Views", "Ingresos", "Estrategia"], languageRows.map(r => [r[0], r[1], r[2], r[3], r[4], badge(r[5], "info")])); }
function channels() { return table(["Canal", "Pais", "Idioma", "Nicho", "Videos", "Views", "Ingresos", "Estado"], channelRows.map(r => [...r.slice(0,7), badge(r[7], toneFor(r[7]))])); }
function calendar() {
  const zones = ["Americas", "LATAM", "Europe", "Brazil", "DACH", "Italy", "Global"];
  return `<article class="card"><h3>Calendario mundial</h3><p class="muted">Bloques simulados por zona horaria y region editorial.</p><div class="calendar-grid">${zones.map((z,i) => `<div class="day-cell"><strong>${z}</strong>${badge("08:00", "ok")} ${badge("13:00", "ok")}<br><br>${badge("17:00", i % 2 ? "warn" : "ok")} ${badge("21:00", "ok")}<p class="muted">${160 + i * 18} videos programados</p></div>`).join("")}</div></article>`;
}
function videos() {
  const names = ["AI Finance", "LATAM Future", "Solar Brazil", "Europe Travel", "AI Learning", "Retail Engine", "Creator Ops", "Global Pulse"];
  return `<div class="video-grid">${names.map((title, i) => `<article class="card video-card"><div class="thumb">${String(i + 1).padStart(2, "0")}</div><div class="video-card-body"><h3>${title}</h3><p class="muted">9:16 · ${i % 2 ? "Publicado" : "Render queue"} · ${["EN","ES","PT","FR","DE","IT"][i % 6]}</p>${badge(i % 2 ? "Publicado" : "Render", i % 2 ? "ok" : "warn")}</div></article>`).join("")}</div>`;
}
function aiEngine() { return table(["IA", "Funcion", "Disponibilidad", "Estado"], aiRows.map(r => [r[0], r[1], r[2], badge(r[3], toneFor(r[3]))])); }
function agents() { return `<div class="grid three">${aiRows.map(([name, fn, uptime, state]) => `<article class="card"><span class="eyebrow">Agente IA</span><h3>${name}</h3><p>${fn}</p><p class="muted">Disponibilidad: ${uptime}</p>${badge(state, toneFor(state))}</article>`).join("")}</div>`; }
function apis() { return table(["API", "Uso futuro", "Modo actual", "Estado"], [["YouTube", "Publicacion y metricas", "Mock", "Pendiente"], ["Instagram", "Reels y metricas", "Mock", "Pendiente"], ["Facebook", "Video y paginas", "Mock", "Pendiente"], ["TikTok", "Publicacion oficial", "Mock", "Pendiente"], ["Storage Cloud", "Assets y renders", "Local prototype", "Simulado"]].map(r => [r[0], r[1], r[2], badge(r[3], toneFor(r[3]))])); }
function monetization() { return `${metricCards()}${table(["Canal", "Pais", "Views", "Ingresos"], channelRows.map(r => [r[0], r[1], r[5], r[6]]))}`; }
function costs() { return table(["Centro de costo", "Costo diario", "Peso", "Estado"], costRows.map(r => [r[0], r[1], r[2], badge(r[3], toneFor(r[3]))])) + barChart("Costos operacionales semanales"); }
function settings() { return `<article class="card"><h3>Configuracion</h3><div class="form-grid">${["Zona horaria matriz", "Modo revision", "Auto publish", "Proveedor IA", "Storage", "Compliance", "Rate limits", "Observabilidad"].map(x => `<div class="field"><label>${x}</label><input readonly value="Configurable en fase futura" /></div>`).join("")}</div></article>`; }
function company() { return `<div class="grid two"><article class="card"><span class="eyebrow">Empresa matriz</span><h3>AppFactoryChile</h3><p>appfactorychile@gmail.com</p><p class="muted">Perfil empresarial preparado para multi-organizacion, permisos, facturacion, auditoria y gobierno operacional global.</p></article>${statusPanel("Gobierno operativo")}</div>`; }
var WORKFLOW_API_BASE = "http://127.0.0.1:8000";
var workflowState = {
  status: "idle",
  error: "",
  workflowId: "",
  channel: null,
  opportunity: null,
  ideas: [],
  selectedIdea: null,
  hooks: [],
  selectedHook: null,
  story: null,
  productionPlan: null,
  ready: null,
  progress: {}
};

function workflowPost(path, body) {
  return fetch(`${WORKFLOW_API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  }).then(response => {
    if (!response.ok) throw new Error(`Workflow backend ${response.status} at ${path}`);
    return response.json();
  });
}

function syncWorkflowBase(response) {
  workflowState.workflowId = response.workflow_id || workflowState.workflowId;
  workflowState.progress = response.progress || workflowState.progress;
  workflowState.status = "ready";
  workflowState.error = "";
}

function workflowPayloadFromForm() {
  const get = id => document.getElementById(id)?.value.trim() || "";
  const mode = document.querySelector('input[name="workflowMode"]:checked')?.value || "manual";
  return {
    name: get("wfName"),
    country: get("wfCountry"),
    language: get("wfLanguage"),
    niche: get("wfNiche"),
    description: get("wfDescription"),
    daily_video_count: Number(get("wfDailyVideos") || 8),
    platforms: get("wfPlatforms").split(",").map(item => item.trim()).filter(Boolean),
    mode
  };
}

async function runWorkflowAction(action, payload = {}) {
  try {
    workflowState.status = "loading";
    workflowState.error = "";
    renderScreen("mvp-workflow");
    let response;
    if (action === "create-channel") {
      response = await workflowPost("/api/workflow/create-channel", workflowPayloadFromForm());
      syncWorkflowBase(response);
      workflowState.channel = response.channel;
    }
    if (action === "analyze-opportunity") {
      response = await workflowPost("/api/workflow/analyze-opportunity", { workflow_id: workflowState.workflowId });
      syncWorkflowBase(response);
      workflowState.opportunity = response;
    }
    if (action === "generate-ideas") {
      response = await workflowPost("/api/workflow/generate-ideas", { workflow_id: workflowState.workflowId });
      syncWorkflowBase(response);
      workflowState.ideas = response.ideas;
    }
    if (action === "choose-idea") {
      response = await workflowPost("/api/workflow/choose-idea", { workflow_id: workflowState.workflowId, idea_id: payload.ideaId });
      syncWorkflowBase(response);
      workflowState.selectedIdea = response.selected_idea;
    }
    if (action === "generate-hooks") {
      response = await workflowPost("/api/workflow/generate-hooks", { workflow_id: workflowState.workflowId });
      syncWorkflowBase(response);
      workflowState.hooks = response.hooks;
    }
    if (action === "choose-hook") {
      response = await workflowPost("/api/workflow/choose-hook", { workflow_id: workflowState.workflowId, hook_id: payload.hookId });
      syncWorkflowBase(response);
      workflowState.selectedHook = response.selected_hook;
    }
    if (action === "generate-story") {
      response = await workflowPost("/api/workflow/generate-story", { workflow_id: workflowState.workflowId });
      syncWorkflowBase(response);
      workflowState.story = response;
    }
    if (action === "generate-production-plan") {
      response = await workflowPost("/api/workflow/generate-production-plan", { workflow_id: workflowState.workflowId });
      syncWorkflowBase(response);
      workflowState.productionPlan = response;
    }
    if (action === "ready-to-generate") {
      response = await workflowPost("/api/workflow/ready-to-generate", { workflow_id: workflowState.workflowId });
      syncWorkflowBase(response);
      workflowState.ready = response;
    }
    renderScreen("mvp-workflow");
  } catch (error) {
    workflowState.status = "error";
    workflowState.error = error.message;
    renderScreen("mvp-workflow");
  }
}

function workflowProgressBar() {
  const steps = [["channel", "Canal"], ["opportunity", "Oportunidad"], ["ideas", "Ideas"], ["idea_selected", "Idea"], ["hooks", "Hook"], ["storyboard", "Storyboard"], ["production", "Produccion"], ["ready", "Listo"]];
  return `<article class="card workflow-progress"><span class="eyebrow">First Complete User Flow</span><h3>Canal -> Oportunidad -> Ideas -> Hook -> Storyboard -> Produccion -> Listo</h3><div class="workflow-steps">${steps.map(([key, label]) => `<span class="${workflowState.progress[key] ? "done" : ""}">${label} ${workflowState.progress[key] ? "OK" : ""}</span>`).join("")}</div>${workflowState.error ? `<p class="muted workflow-error">${workflowState.error}</p>` : ""}</article>`;
}

function workflowChannelForm() {
  return `<article class="card"><span class="eyebrow">Paso 1</span><h3>Crear Canal</h3><div class="form-grid"><div class="field"><label>Nombre</label><input id="wfName" value="Futuro Latino IA" /></div><div class="field"><label>Pais</label><input id="wfCountry" value="Mexico" /></div><div class="field"><label>Idioma</label><input id="wfLanguage" value="Spanish" /></div><div class="field"><label>Nicho</label><input id="wfNiche" value="Technology" /></div><div class="field"><label>Videos diarios</label><input id="wfDailyVideos" type="number" value="8" min="1" max="50" /></div><div class="field"><label>Plataformas</label><input id="wfPlatforms" value="YouTube Shorts, Instagram Reels, TikTok" /></div><div class="field workflow-span"><label>Descripcion</label><input id="wfDescription" value="AI tools for small businesses" /></div><div class="field"><label>Modo</label><div class="mode-toggle"><label><input type="radio" name="workflowMode" value="automatic" /> Automatico</label><label><input type="radio" name="workflowMode" value="manual" checked /> Manual</label></div></div></div><button class="primary-btn" type="button" data-workflow-action="create-channel">Guardar canal</button></article>`;
}

function workflowOpportunityPanel() {
  if (!workflowState.channel) return "";
  const op = workflowState.opportunity;
  return `<article class="card"><span class="eyebrow">Paso 2</span><h3>Analizar Oportunidades</h3>${op ? `<div class="grid metrics"><article class="metric-card"><small>Opportunity Score</small><span class="metric-value">${op.opportunity_score}</span><span class="delta">${op.potential}</span></article><article class="metric-card"><small>Competencia</small><span class="metric-value">${op.competition}</span><span class="delta">Mercado</span></article><article class="metric-card"><small>Monetizacion</small><span class="metric-value">${op.monetization}</span><span class="delta">Potencial</span></article><article class="metric-card"><small>Horario ideal</small><span class="metric-value">${op.ideal_time}</span><span class="delta">Local</span></article></div><p class="muted">${op.trend}</p>` : `<p class="muted">El Content Brain analizara el canal guardado y devolvera un score mock realista.</p>`}<button class="primary-btn" type="button" data-workflow-action="analyze-opportunity">Analizar oportunidad</button></article>`;
}

function workflowIdeasPanel() {
  if (!workflowState.opportunity) return "";
  return `<article class="card"><span class="eyebrow">Paso 3 y 4</span><h3>Generar Ideas y elegir una</h3>${workflowState.ideas.length ? `<div class="workflow-idea-grid">${workflowState.ideas.map(idea => `<article class="workflow-choice ${workflowState.selectedIdea?.id === idea.id ? "selected" : ""}"><strong>${idea.title}</strong><p>${idea.value}</p><div class="style-meta"><span>Curiosidad ${idea.curiosity}</span><span>${idea.emotion}</span><span>Viral ${idea.viral_level}</span><span>Monetizacion ${idea.monetization}</span><span>Retencion ${idea.retention}</span></div><button class="ghost-btn" type="button" data-workflow-action="choose-idea" data-idea-id="${idea.id}">Elegir idea</button></article>`).join("")}</div>` : `<p class="muted">Genera 10 ideas desde el backend y luego selecciona una para continuar.</p>`}<button class="primary-btn" type="button" data-workflow-action="generate-ideas">Generar 10 ideas</button></article>`;
}

function workflowHooksPanel() {
  if (!workflowState.selectedIdea) return "";
  return `<article class="card"><span class="eyebrow">Paso 5</span><h3>Generar Hook</h3>${workflowState.hooks.length ? `<div class="hook-stack">${workflowState.hooks.map(hook => `<div class="hook-card ${workflowState.selectedHook?.id === hook.id ? "selected" : ""}"><strong>${hook.hook}</strong><span>${hook.score}/100</span><small>${hook.emotion} · ${hook.retention}</small><button class="ghost-btn" type="button" data-workflow-action="choose-hook" data-hook-id="${hook.id}">Seleccionar hook</button></div>`).join("")}</div>` : `<p class="muted">El backend generara 5 opciones de hook para la idea seleccionada.</p>`}<button class="primary-btn" type="button" data-workflow-action="generate-hooks">Generar hooks</button></article>`;
}

function workflowStoryPanel() {
  if (!workflowState.selectedHook) return "";
  const story = workflowState.story;
  return `<article class="card"><span class="eyebrow">Paso 6 y 7</span><h3>Story Strategy y Storyboard</h3>${story ? `<div class="director-row"><span>Objetivo</span><strong>${story.objective}</strong></div><div class="director-row"><span>Narrador</span><strong>${story.narrator}</strong></div><div class="director-row"><span>Personaje</span><strong>${story.character}</strong></div><div class="director-row"><span>Escenario</span><strong>${story.scenario}</strong></div><div class="director-row"><span>Tono</span><strong>${story.tone}</strong></div><div class="director-row"><span>Duracion</span><strong>${story.duration_seconds}s</strong></div><div class="director-row"><span>Estilo</span><strong>${story.style}</strong></div><div class="scene-grid">${story.scenes.map(scene => `<article class="scene-card"><span>${scene.scene}</span><strong>${scene.visual}</strong><p>${scene.narration}</p><small>${scene.subtitles}</small></article>`).join("")}</div><p class="muted"><b>Narracion:</b> ${story.narration}</p><p class="muted"><b>CTA:</b> ${story.cta}</p>` : `<p class="muted">Genera objetivo, narrador, personaje, escenario, tono, duracion, estilo y storyboard.</p>`}<button class="primary-btn" type="button" data-workflow-action="generate-story">Generar Story Strategy</button></article>`;
}

function workflowProductionPanel() {
  if (!workflowState.story) return "";
  const plan = workflowState.productionPlan;
  return `<article class="card"><span class="eyebrow">Paso 8</span><h3>Production Plan</h3>${plan ? `<div class="grid two"><article><div class="director-row"><span>Narrador</span><strong>${plan.narrator}</strong></div><div class="director-row"><span>Tipo de voz</span><strong>${plan.voice_type}</strong></div><div class="director-row"><span>Formato</span><strong>${plan.format}</strong></div><div class="director-row"><span>Plataformas</span><strong>${plan.platforms.join(", ")}</strong></div><div class="director-row"><span>Idioma</span><strong>${plan.language}</strong></div></article><article><div class="director-row"><span>Musica</span><strong>${plan.music}</strong></div><div class="director-row"><span>Iluminacion</span><strong>${plan.lighting}</strong></div><div class="director-row"><span>Camara</span><strong>${plan.camera_movement}</strong></div><div class="director-row"><span>Color</span><strong>${plan.color}</strong></div><div class="director-row"><span>Ritmo</span><strong>${plan.rhythm}</strong></div></article></div>` : `<p class="muted">Genera plan de produccion sin crear video, audio ni imagenes.</p>`}<button class="primary-btn" type="button" data-workflow-action="generate-production-plan">Generar Production Plan</button></article>`;
}

function workflowReadyPanel() {
  if (!workflowState.productionPlan) return "";
  return `<article class="card ready-card"><span class="eyebrow">Paso 9</span><h3>${workflowState.ready?.message || "READY TO GENERATE"}</h3><p>No se generara video todavia. El flujo queda preparado para una fase futura de video, audio, imagenes, subtitulos reales y publicacion.</p>${workflowState.ready ? `<div class="guardrail-list">${workflowState.ready.next_locked_steps.map(step => `<span>${step}</span>`).join("")}</div>${badge("Listo", "ok")}` : `<button class="primary-btn" type="button" data-workflow-action="ready-to-generate">Marcar listo para generar</button>`}</article>`;
}

function mvpWorkflow() {
  return `${workflowProgressBar()}${workflowChannelForm()}${workflowOpportunityPanel()}${workflowIdeasPanel()}${workflowHooksPanel()}${workflowStoryPanel()}${workflowProductionPanel()}${workflowReadyPanel()}`;
}
var CONTENT_BRAIN_API_BASE = "http://127.0.0.1:8000";
var contentBrainState = {
  status: "idle",
  step: "Ready",
  error: "",
  analysis: null,
  recommendation: null,
  storyboard: null,
  productionPlan: null
};
var contentBrainRequest = {
  topic: "AI tools for small businesses",
  country: "Mexico",
  language: "Spanish",
  niche: "Technology"
};

function contentBrainPost(path) {
  return fetch(`${CONTENT_BRAIN_API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(contentBrainRequest)
  }).then(response => {
    if (!response.ok) throw new Error(`Backend ${response.status} at ${path}`);
    return response.json();
  });
}

async function runContentBrainSimulation() {
  try {
    contentBrainState = { ...contentBrainState, status: "loading", step: "Opportunity -> Research", error: "" };
    renderScreen(location.hash.replace("#", "") || "dashboard");
    const analysis = await contentBrainPost("/api/content-brain/analyze");

    contentBrainState = { ...contentBrainState, analysis, step: "Editorial Analysis" };
    renderScreen(location.hash.replace("#", "") || "dashboard");
    const recommendation = await contentBrainPost("/api/content-brain/recommend");

    contentBrainState = { ...contentBrainState, recommendation, step: "Story Strategy" };
    renderScreen(location.hash.replace("#", "") || "dashboard");
    const storyboard = await contentBrainPost("/api/content-brain/storyboard");

    contentBrainState = { ...contentBrainState, storyboard, step: "Production Plan" };
    renderScreen(location.hash.replace("#", "") || "dashboard");
    const productionPlan = await contentBrainPost("/api/content-brain/production-plan");

    contentBrainState = { status: "ready", step: "Complete", error: "", analysis, recommendation, storyboard, productionPlan };
    renderScreen(location.hash.replace("#", "") || "dashboard");
  } catch (error) {
    contentBrainState = { ...contentBrainState, status: "error", error: error.message, step: "Backend unavailable" };
    renderScreen(location.hash.replace("#", "") || "dashboard");
  }
}

function ensureContentBrainData() {
  if (contentBrainState.status === "idle") runContentBrainSimulation();
}

function contentBrainControl() {
  const state = contentBrainState.status === "ready" ? "Conectado" : contentBrainState.status === "loading" ? contentBrainState.step : contentBrainState.status === "error" ? "Error" : "Listo";
  const tone = contentBrainState.status === "ready" ? "ok" : contentBrainState.status === "error" ? "warn" : "info";
  return `<article class="card brain-control"><div><span class="eyebrow">Content Brain Backend</span><h3>Simular creacion completa</h3><p>Opportunity -> Research -> Ideas -> Ranking -> Story Strategy -> Production Plan desde FastAPI mock.</p><div class="guardrail-list"><span>${contentBrainRequest.country}</span><span>${contentBrainRequest.language}</span><span>${contentBrainRequest.niche}</span><span>${contentBrainRequest.topic}</span></div>${contentBrainState.error ? `<p class="muted brain-error">${contentBrainState.error}</p>` : ""}</div><div class="brain-actions">${badge(state, tone)}<button class="primary-btn" type="button" data-run-brain>Simular creacion completa</button></div></article>`;
}

function requireBrainData() {
  ensureContentBrainData();
  if (contentBrainState.status === "ready") return "";
  if (contentBrainState.status === "error") return `${contentBrainControl()}<article class="card"><h3>Backend no disponible</h3><p class="muted">Ejecuta el backend en http://127.0.0.1:8000 y vuelve a presionar Simular creacion completa.</p></article>`;
  return `${contentBrainControl()}<article class="card"><h3>Esperando respuesta del Content Brain</h3><p class="muted">El prototipo esta solicitando datos al backend mock mediante fetch().</p></article>`;
}

function brainScoreGridFromRanking(ranking) {
  return scoreGrid(ranking.slice(0, 4).map(item => [item.title, item.score, item.reason]));
}

function storyDirector() {
  const fallback = requireBrainData();
  if (fallback) return fallback;
  const strategy = contentBrainState.analysis.story_strategy;
  const audience = contentBrainState.analysis.audience_profile;
  const rows = [
    ["Idea seleccionada", strategy.selected_idea],
    ["Publico objetivo", audience.target_audience],
    ["Pais", audience.country],
    ["Idioma", audience.language],
    ["Emocion principal", strategy.emotional_goal],
    ["Objetivo del video", strategy.narrative_arc],
    ["Personaje recomendado", strategy.character],
    ["Estilo visual", strategy.visual_style],
    ["Duracion", `${strategy.recommended_duration_seconds}s`],
    ["Tono", strategy.tone]
  ];
  return `${contentBrainControl()}<div class="grid two"><article class="card director-panel"><span class="eyebrow">Story Director AI</span><h3>La IA transforma una oportunidad en una estrategia narrativa.</h3>${rows.map(([label, value], index) => `<div class="director-row"><span>${label}</span><strong>${value}</strong>${index === rows.length - 1 ? badge("Backend", "ok") : ""}</div>`).join("")}</article><article class="card"><span class="eyebrow">Ranking creativo</span><h3>Ideas priorizadas por el Content Brain</h3>${brainScoreGridFromRanking(contentBrainState.analysis.ranking)}</article></div>`;
}

function ideaLab() {
  const fallback = requireBrainData();
  if (fallback) return fallback;
  const analysis = contentBrainState.analysis;
  return `${contentBrainControl()}<article class="card"><span class="eyebrow">Idea Lab</span><h3>10 ideas generadas por backend mock</h3><p class="muted">Cada idea sale del Content Brain y luego entra al ranking editorial.</p>${analysis.ideas.map((idea, index) => `<div class="entity-row"><div><span class="entity-title">${String(index + 1).padStart(2, "0")} · ${idea.title}</span><span class="entity-meta">${idea.angle} · Emocion: ${idea.emotion} · ${idea.target_duration_seconds}s · ${idea.value_promise}</span></div>${badge(index === 0 ? "Idea" : "Mock", index === 0 ? "ok" : "info")}</div>`).join("")}</article>${table(["Rank", "Idea", "Score", "Curiosidad", "Conversacion", "Monetizacion"], analysis.ranking.map(item => [item.rank, item.title, `${item.score}/100`, `${item.curiosity_score}/100`, `${item.conversation_score}/100`, `${item.monetization_score}/100`]))}`;
}

function contentPipeline() {
  const fallback = requireBrainData();
  if (fallback) return fallback;
  const analysis = contentBrainState.analysis;
  const stages = [
    ["Opportunity", `${analysis.opportunity_score}/100`, "Content Brain"],
    ["Research", analysis.research_summary.summary, "Research AI"],
    ["Idea Generation", `${analysis.ideas.length} ideas`, "Idea Generator AI"],
    ["Idea Ranking", analysis.best_idea.title, "Ranking AI"],
    ["Editorial Analysis", contentBrainState.recommendation.why_this_idea_is_better, "Editorial AI"],
    ["Audience Analysis", analysis.audience_profile.target_audience, "Audience AI"],
    ["Hook Generation", `${analysis.hooks.length} hooks`, "Hook AI"],
    ["Story Strategy", analysis.story_strategy.narrative_arc, "Story Director AI"],
    ["Video Strategy", analysis.story_strategy.visual_style, "Video Strategy AI"],
    ["Production Plan", analysis.production_plan.format, "Production Planner AI"]
  ];
  return `${contentBrainControl()}<article class="card"><span class="eyebrow">Content Pipeline</span><h3>Opportunity -> Production Plan generado desde FastAPI</h3><div class="pipeline-flow">${stages.map(([stage, detail, owner], index) => `<div class="flow-step"><span class="flow-index">${String(index + 1).padStart(2, "0")}</span><strong>${stage}</strong><small>${owner}</small><p class="muted">${detail}</p><div>${badge("Backend", "ok")}<em>Mock real</em></div></div>`).join("")}</div></article>`;
}

function editorialDirector(compact = false) {
  const fallback = requireBrainData();
  if (fallback) return fallback;
  const rec = contentBrainState.recommendation;
  const rows = [
    ["Mejor idea", rec.best_idea],
    ["Por que es mejor", rec.why_this_idea_is_better],
    ["Emocion", rec.target_emotion],
    ["Duracion recomendada", `${rec.recommended_duration_seconds}s`],
    ["Personaje", rec.recommended_character],
    ["Estilo visual", rec.recommended_visual_style],
    ["Tono", rec.recommended_tone],
    ["Nivel de curiosidad", `${rec.curiosity_level}/100`],
    ["Potencial de conversacion", `${rec.conversation_potential}/100`],
    ["Potencial de monetizacion", `${rec.monetization_potential}/100`]
  ];
  const panel = `<article class="card director-panel"><span class="eyebrow">Editorial Director AI</span><h3>Recomendacion editorial desde Content Brain</h3>${rows.map(([label, value], index) => `<div class="director-row"><span>${label}</span><strong>${value}</strong>${index === rows.length - 1 ? badge("Recomendado", "ok") : ""}</div>`).join("")}</article>`;
  return compact ? panel : `${contentBrainControl()}${panel}`;
}
function renderScreen(id) {
  const screen = screens.find(s => s.id === id) || screens[1];
  pageTitle.textContent = screen.label;
  document.querySelectorAll(".nav-link").forEach(a => a.classList.toggle("active", a.dataset.id === screen.id));
  const routes = {
    login,
    dashboard,
    "mvp-workflow": mvpWorkflow,
    intelligence,
    "global-intelligence": globalIntelligence,
    "digital-factory": digitalFactory,
    "global-factory": globalFactory,
    "end-to-end-pipeline": endToEndPipeline,
    "video-factory-live": videoFactoryLive,
    "ai-workers": aiWorkers,
    "multi-channel-manager": multiChannelManager,
    "world-scheduler": worldSchedulerFactory,
    "factory-monetization": factoryMonetization,
    "mission-control": missionControl,
    "full-video-journey": fullVideoJourney,
    "executive-overview": executiveOverview,
    "learning-engine": learningEngine,
    "memory-engine": memoryEngine,
    "channel-memory": channelMemory,
    "country-memory": countryMemory,
    "language-memory": languageMemory,
    "experiment-engine": experimentEngine,
    "creative-evolution": creativeEvolution,
    "global-knowledge": globalKnowledge,
    "ai-self-improvement": aiSelfImprovement,
    "global-learning-map": learningMap,
    "next-best-action": nextBestAction,
    "story-director": storyDirector,
    "video-style-lab": videoStyleLab,
    "character-scene": characterSceneBuilder,
    "hook-retention": hookRetentionSimulator,
    "vertical-blueprint": verticalBlueprint,
    "smart-duration": smartDurationEngine,
    "attention-engine": attentionEngine,
    "retention-engine": retentionEngine,
    "opportunity-radar": opportunityRadar,
    "competitor-intelligence": competitorIntelligence,
    "content-pipeline": contentPipeline,
    "editorial-director": editorialDirector,
    "content-heatmap": globalContentHeatmap,
    "decision-timeline": aiDecisionTimeline,
    "quality-dashboard": qualityDashboard,
    "viral-psychology": viralPsychology,
    "channel-dna": channelDna,
    "quality-gate": qualityGate,
    "entertainment-scoring": entertainmentScoring,
    "idea-lab": ideaLab,
    "hook-builder": hookBuilder,
    "curiosity-map": curiosityMap,
    trends,
    "trend-country": byCountry,
    "trend-language": byLanguage,
    channels,
    countries: byCountry,
    languages: byLanguage,
    calendar,
    videos,
    queue: () => queueView("Estado de renderizado mundial"),
    publish: () => table(["Region", "Plataforma", "Pendientes", "Estado"], [["US", "YouTube", "84", "Simulado"], ["LATAM", "Instagram", "126", "Simulado"], ["EU", "TikTok", "92", "Pendiente API"], ["BR", "Facebook", "48", "Simulado"]].map(r => [r[0], r[1], r[2], badge(r[3], toneFor(r[3]))])),
    "ai-engine": aiEngine,
    agents,
    automation: () => pipeline() + calendar(),
    apis,
    monetization,
    costs,
    system: () => `<div class="grid two">${statusPanel("Estado de servidores")}${queueView("Carga por cluster")}</div>`,
    settings,
    company
  };
  view.innerHTML = (routes[screen.id] || dashboard)();
  bindSoonButtons();
}
function bindSoonButtons() {
  document.querySelectorAll("[data-soon]").forEach(btn => btn.addEventListener("click", () => {
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), 1500);
  }));
  document.querySelectorAll("[data-run-brain]").forEach(btn => btn.addEventListener("click", () => runContentBrainSimulation()));
  document.querySelectorAll("[data-workflow-action]").forEach(btn => btn.addEventListener("click", () => runWorkflowAction(btn.dataset.workflowAction, { ideaId: btn.dataset.ideaId, hookId: btn.dataset.hookId })));
}
function buildNav() {
  sideNav.innerHTML = screens.map(screen => `<a class="nav-link" href="#${screen.id}" data-id="${screen.id}" title="${screen.label}"><span class="nav-icon">${screen.icon}</span><span>${screen.label}</span><small class="nav-kpi">${screen.kpi}</small></a>`).join("");
}
function route() {
  renderScreen(location.hash.replace("#", "") || "dashboard");
  sidebar.classList.remove("open");
}
document.getElementById("menuToggle").addEventListener("click", () => sidebar.classList.toggle("open"));
window.addEventListener("hashchange", route);
buildNav();
route();







