import React from 'react'
import {Link} from 'react-router-dom'

function Header(){
    return (
        <header className="container mx-auto">
            <br></br>
            <Link to="/" className="font-bold text-2 mb-3  inline-flex items-center justify-center px-5 py-3 border border-transparent font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
                Kiwi Doors
            </Link>

        </header>
    )
}

export default Header