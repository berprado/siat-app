import { useEffect, useState } from 'react'

function App() {
  const [mensaje, setMensaje] = useState('')

  useEffect(() => {
    fetch('http://localhost:8000/soap/verificar-comunicacion')
      .then(res => res.json())
      .then(data => setMensaje(data.resultado || 'Sin respuesta'))
  }, [])
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Verificar Comunicación SIAT</h1>
      <p className="text-lg">{mensaje}</p>
    </div>
  )
}

export default App
