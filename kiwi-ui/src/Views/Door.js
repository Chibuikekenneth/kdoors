import React from 'react'
import { useParams } from 'react-router-dom'
import Loader from '../Components/Loader'
import { useAxiosGet } from '../Hooks/HttpRequests'
import UserCard from '../Components/UserCard'
import User from './User'

function Door(){
    const { id } = useParams()

    const doorUrl = `http://localhost:5000/api/v1/doors/${id}`
    const permissionUrl = `http://localhost:5000/api/v1/permissions/${id}`
 
    let door = useAxiosGet(doorUrl)
    let permissions = useAxiosGet(permissionUrl)

    let doorcontent = null
    let permissionContent = null

    if(door.error){
        doorcontent = <div>
            <div className="bg-red-300 p-3">
                There was an error please refresh or try again later.
            </div>
        </div>
    }

    if(permissions.error){
      permissionContent = <div>
          <div className="bg-red-300 p-3">
              There was an error loading users, please refresh or try again later.
          </div>
      </div>
  }

    if(door.loading){
        doorcontent = <Loader></Loader>
    }

    if(door.data){
        doorcontent = 
        <div>
        <div className="container mx-auto">
        <div className="bg-white shadow overflow-hidden sm:rounded-lg">
          <div className="px-4 py-5 sm:px-6">
            <h3 className="text-lg leading-9 font-medium text-gray-900">{door.data.name}</h3>
          </div>
          <div className="border-t border-gray-200">
            <dl>
              <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                <dt className="text-sm font-medium text-gray-500">Address</dt>
                <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{door.data.address.street}, {door.data.address.city}</dd>
              </div>
              <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                <dt className="text-sm font-medium text-gray-500">Last Communcation Time</dt>
                <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{door.data.last_communication_time ? door.data.last_communication_time : 'nill'}</dd>
              </div>
            </dl>
          </div>
        </div>

        <br></br>  
        <br></br>  
            <div className="font-bold text-2 mb-3  inline-flex items-center justify-center px-5 py-3 border border-transparent font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
                  <div className="">
                      <h3 className="">Add users to {door.data.name}</h3>
                  </div>
            </div>
          <User doorid = {door.data.id}/>
        <br></br>

        <br></br> 
          <div className="bg-white shadow overflow-hidden sm:rounded-lg">
                <div className="px-4 py-5 sm:px-6">
                    <h3 className="text-lg leading-6 font-medium text-gray-900">Below are Users with access to {door.data.name}</h3>
                </div>
                
          </div>
        <br></br>    
        </div>
        </div>  
    }

    if(permissions.data){
        permissionContent = 
        permissions.data.map((permission) => 
            <div key={permission.id} className="flex-no-shrink w-full md:w-1/3 md:px-3">
            <UserCard 
                permission={permission}
            />
        </div>)
    }

    return (
        <div className="container mx-auto">
            {doorcontent}
          
            <div>
              <div className="md:flex flex-wrap md:-mx-3">
                {permissionContent}
              </div>
            </div>
        </div>
    )

}

export default Door

